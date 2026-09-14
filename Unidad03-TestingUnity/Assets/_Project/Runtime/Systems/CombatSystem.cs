using UnityEngine;

public class CombatSystem : MonoBehaviour
{
    [SerializeField] private float cooldownSeconds = 1f;

    [Tooltip("Probabilidad de critico (x2 dano). En 0 por defecto para que la demo sea " +
             "predecible: cada golpe saca siempre 'damage' de vida, sin variacion aleatoria. " +
             "Subir este valor a mano en el Inspector si se quiere mostrar el critico en vivo.")]
    [SerializeField] private float criticalChance = 0f;

    [Tooltip("CRYPT-201 (docs/unidad03/02-caso-practico-testing-videojuego.md, Seccion F). " +
             "Activado, el 'critico' duplica el dano llamando TakeDamage() dos veces en vez de " +
             "aplicar una sola vez el monto ya calculado. Se deja como toggle de Inspector para " +
             "poder mostrar la regresion en vivo sin tener que editar el codigo delante de la clase.")]
    [SerializeField] private bool enableCriticalHitBug = false;

    private float lastAttackTime = -999f;

    public bool TryAttack(PlayerHealth target, int damage)
    {
        if (Time.time - lastAttackTime < cooldownSeconds)
        {
            return false;
        }

        if (enableCriticalHitBug)
        {
            target.TakeDamage(damage);
            if (Random.value < criticalChance)
            {
                target.TakeDamage(damage); // bug: duplica el golpe en vez de aumentarlo
            }
        }
        else
        {
            int finalDamage = Random.value < criticalChance ? damage * 2 : damage;
            target.TakeDamage(finalDamage);
        }

        lastAttackTime = Time.time;
        return true;
    }

    public float CooldownFraction => Mathf.Clamp01((Time.time - lastAttackTime) / cooldownSeconds);
}
