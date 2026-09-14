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

    private CombatSystem combatSystem;

    private void Awake()
    {
        combatSystem = GetComponent<CombatSystem>();
    }

    private void Update()
    {
        HandleMovement();
        HandleAttackInput();
        UpdateCooldownUI();
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

        combatSystem.TryAttack(enemy.Health, attackDamage);
    }

    private void UpdateCooldownUI()
    {
        if (cooldownSlider != null)
        {
            cooldownSlider.value = combatSystem.CooldownFraction;
        }
    }
}
