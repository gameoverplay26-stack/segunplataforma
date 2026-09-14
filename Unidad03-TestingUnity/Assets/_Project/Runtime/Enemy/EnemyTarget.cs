using System.Collections;
using UnityEngine;
using UnityEngine.UI;

public class EnemyTarget : MonoBehaviour
{
    [SerializeField] private int maxHealth = 100; // con attackDamage=20 por defecto en PlayerController, son 5 golpes minimo (menos si hay critico)
    [SerializeField] private Slider healthSlider;
    [SerializeField] private Text healthLabel;
    [SerializeField] private Renderer bodyRenderer;

    private static readonly Color AliveColor = new Color(0.75f, 0.2f, 0.2f);
    private static readonly Color DeadColor = new Color(0.35f, 0.35f, 0.35f);
    private static readonly Color FlashColor = Color.white;
    private const float FlashDuration = 0.1f;
    private const float FlashScale = 1.15f;
    private const float KnockbackDistance = 1f;

    // La camara top-down tiene orthographicSize=7 (mitad vertical, mapea a Z, siempre 7).
    // La mitad horizontal (mapea a X) depende del aspect ratio de la ventana Game y puede
    // ser MENOR a 7 si la ventana no es panoramica — por eso el limite en X se deja bien
    // por debajo de 7, no solo dentro del piso, para que el Enemy nunca quede fuera de
    // cuadro por la acumulacion de varios retrocesos seguidos en la misma direccion.
    private const float GroundBoundX = 5f;
    private const float GroundBoundZ = 5f;

    public PlayerHealth Health { get; private set; }
    public bool IsDead => Health.IsDead;

    private bool isFlashing;
    private Vector3 spawnPosition;
    private Vector3 spawnScale;

    private void Awake()
    {
        spawnPosition = transform.position;
        spawnScale = transform.localScale;
        ResetEnemy();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            ResetEnemy();
        }

        UpdateUI();
    }

    public void ResetEnemy()
    {
        // Cancela cualquier retroceso en curso — si no, la corutina puede seguir
        // moviendolo un par de frames mas y pisar la posicion que acabamos de restaurar.
        StopCoroutine(nameof(HitReactionRoutine));
        isFlashing = false;
        transform.position = spawnPosition;
        transform.localScale = spawnScale;

        Health = new PlayerHealth(maxHealth);

        if (healthSlider != null)
        {
            healthSlider.maxValue = maxHealth;
        }

        UpdateUI();
    }

    // knockbackDirection: sentido contrario al golpe (del atacante hacia el objetivo) —
    // el enemigo retrocede una vez por cada disparo que conecta.
    public void PlayHitReaction(Vector3 knockbackDirection)
    {
        if (bodyRenderer == null)
        {
            return;
        }

        StopCoroutine(nameof(HitReactionRoutine));
        StartCoroutine("HitReactionRoutine", knockbackDirection);
    }

    private IEnumerator HitReactionRoutine(Vector3 knockbackDirection)
    {
        isFlashing = true;
        var originalScale = transform.localScale;
        var startPosition = transform.position;
        var targetPosition = ClampToGround(startPosition + knockbackDirection.normalized * KnockbackDistance);

        bodyRenderer.material.color = FlashColor;
        transform.localScale = originalScale * FlashScale;

        float elapsed = 0f;
        while (elapsed < FlashDuration)
        {
            elapsed += Time.deltaTime;
            transform.position = Vector3.Lerp(startPosition, targetPosition, elapsed / FlashDuration);
            yield return null;
        }

        transform.localScale = originalScale;
        isFlashing = false;
    }

    private static Vector3 ClampToGround(Vector3 position)
    {
        position.x = Mathf.Clamp(position.x, -GroundBoundX, GroundBoundX);
        position.z = Mathf.Clamp(position.z, -GroundBoundZ, GroundBoundZ);
        return position;
    }

    private void UpdateUI()
    {
        if (healthSlider != null)
        {
            healthSlider.value = Health.CurrentHealth;
        }

        if (healthLabel != null)
        {
            healthLabel.text = Health.IsDead
                ? $"Enemigo: {Health.CurrentHealth}/{Health.MaxHealth} (DERROTADO)"
                : $"Enemigo: {Health.CurrentHealth}/{Health.MaxHealth}";
        }

        // Mientras isFlashing, HitReactionRoutine controla el color — si lo pisaramos aca
        // cada frame, el flash nunca se llegaria a ver (Update corre mas seguido que dura el flash).
        if (bodyRenderer != null && !isFlashing)
        {
            bodyRenderer.material.color = Health.IsDead ? DeadColor : AliveColor;
        }
    }
}
