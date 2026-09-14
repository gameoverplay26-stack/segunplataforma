using System.Collections;
using UnityEngine;
using UnityEngine.UI;

[RequireComponent(typeof(CombatSystem))]
public class PlayerController : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 4f;
    [SerializeField] private float attackRange = 2.5f;
    [SerializeField] private int attackDamage = 20;
    [SerializeField] private EnemyTarget enemy;
    [SerializeField] private Slider cooldownSlider;

    private const int RangeCircleSegments = 40;
    private const float ProjectileDuration = 0.15f;
    private static readonly Color OutOfRangeColor = new Color(1f, 1f, 1f, 0.25f);
    private static readonly Color InRangeReadyColor = new Color(0.3f, 1f, 0.3f, 0.6f);
    private static readonly Color InRangeCooldownColor = new Color(1f, 0.8f, 0.2f, 0.6f);

    private CombatSystem combatSystem;
    private LineRenderer rangeIndicator;

    private void Awake()
    {
        combatSystem = GetComponent<CombatSystem>();
        rangeIndicator = BuildRangeIndicator();
    }

    private void Update()
    {
        HandleMovement();
        HandleAttackInput();
        UpdateCooldownUI();
        UpdateRangeIndicator();
    }

    private void HandleMovement()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        var move = new Vector3(horizontal, 0f, vertical) * (moveSpeed * Time.deltaTime);
        transform.Translate(move, Space.World);
    }

    private void HandleAttackInput()
    {
        if (!Input.GetKeyDown(KeyCode.Space) || enemy == null || enemy.IsDead)
        {
            return;
        }

        float distance = Vector3.Distance(transform.position, enemy.transform.position);
        if (distance > attackRange)
        {
            return;
        }

        if (combatSystem.TryAttack(enemy.Health, attackDamage))
        {
            StartCoroutine(FireProjectile(enemy));
        }
    }

    private IEnumerator FireProjectile(EnemyTarget target)
    {
        var projectile = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        projectile.name = "AttackProjectile";
        Destroy(projectile.GetComponent<Collider>());
        projectile.transform.localScale = Vector3.one * 0.3f;
        projectile.GetComponent<Renderer>().material.color = new Color(1f, 0.6f, 0.1f);

        var start = transform.position + Vector3.up * 0.5f;
        var elapsed = 0f;

        while (elapsed < ProjectileDuration)
        {
            elapsed += Time.deltaTime;
            var end = target.transform.position + Vector3.up * 0.5f;
            projectile.transform.position = Vector3.Lerp(start, end, elapsed / ProjectileDuration);
            yield return null;
        }

        Destroy(projectile);
        var knockbackDirection = target.transform.position - transform.position;
        target.PlayHitReaction(knockbackDirection);
    }

    private void UpdateCooldownUI()
    {
        if (cooldownSlider != null)
        {
            cooldownSlider.value = combatSystem.CooldownFraction;
        }
    }

    private LineRenderer BuildRangeIndicator()
    {
        var indicatorGO = new GameObject("AttackRangeIndicator");
        indicatorGO.transform.SetParent(transform, false);
        indicatorGO.transform.localPosition = new Vector3(0f, -0.95f, 0f);

        var line = indicatorGO.AddComponent<LineRenderer>();
        line.material = new Material(Shader.Find("Sprites/Default"));
        line.useWorldSpace = false;
        line.loop = true;
        line.widthMultiplier = 0.06f;
        line.positionCount = RangeCircleSegments;

        for (int i = 0; i < RangeCircleSegments; i++)
        {
            float angle = 2f * Mathf.PI * i / RangeCircleSegments;
            var point = new Vector3(Mathf.Cos(angle), 0f, Mathf.Sin(angle)) * attackRange;
            line.SetPosition(i, point);
        }

        return line;
    }

    private void UpdateRangeIndicator()
    {
        if (rangeIndicator == null || enemy == null)
        {
            return;
        }

        bool inRange = !enemy.IsDead
            && Vector3.Distance(transform.position, enemy.transform.position) <= attackRange;

        Color color;
        if (!inRange)
        {
            color = OutOfRangeColor;
        }
        else
        {
            color = combatSystem.CooldownFraction >= 1f ? InRangeReadyColor : InRangeCooldownColor;
        }

        rangeIndicator.startColor = color;
        rangeIndicator.endColor = color;
    }
}
