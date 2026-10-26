using UnityEngine;

// v2 (porteo a móvil): el controlador ya no lee dispositivos.
// Recibe la intención (mover, saltar) desde PlayerInputAdapter, o desde un test.
public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float jumpForce = 10f;
    public float doubleJumpForce = 8f;
    public LayerMask groundLayer;
    public Transform groundCheck;

    private Rigidbody2D rb;
    private bool isGroundedBool = false;
    private bool canDoubleJump = false;

    public Animator playeranim;

    // Intención recibida: dirección horizontal (-1, 0, 1) y pedido de salto.
    private float moveX;
    private bool jumpRequested;
    public bool isPaused = false;

    public ParticleSystem footsteps;
    private ParticleSystem.EmissionModule footEmissions;

    public ParticleSystem ImpactEffect;
    private bool wasonGround;

    // El Animator (sr.controller) no tiene el parámetro "isGrounded":
    // escribirlo sin chequear generaba un error por frame (R-PLT-01).
    private bool animHasIsGrounded;

    public bool IsGroundedNow => isGroundedBool;

    private void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        footEmissions = footsteps.emission;
        animHasIsGrounded = HasParameter(playeranim, "isGrounded");
    }

    // Punto de entrada único de la entrada (teclado, gamepad o táctil).
    public void SetIntent(float horizontal, bool jumpPressed)
    {
        moveX = horizontal;
        if (jumpPressed)
        {
            jumpRequested = true;
        }
    }

    private void Update()
    {
        isGroundedBool = IsGrounded();

        if (isGroundedBool)
        {
            canDoubleJump = true; // Reset double jump when grounded
        }

        if (jumpRequested)
        {
            TryJump();
            jumpRequested = false; // Sin buffer de salto (DEC-LAB-007 pendiente)
        }

        SetAnimations();

        if (moveX != 0)
        {
            FlipSprite(moveX);
        }

        //impactEffect

        if (!wasonGround && isGroundedBool)
        {
            ImpactEffect.gameObject.SetActive(true);
            ImpactEffect.Stop();
            ImpactEffect.transform.position = new Vector2(footsteps.transform.position.x, footsteps.transform.position.y - 0.2f);
            ImpactEffect.Play();
        }

        wasonGround = isGroundedBool;
    }

    private void TryJump()
    {
        if (isGroundedBool)
        {
            Jump(jumpForce);
            Sfx.Play(Sfx.Kind.Jump);
        }
        else if (canDoubleJump)
        {
            Jump(doubleJumpForce);
            Sfx.Play(Sfx.Kind.DoubleJump);
            canDoubleJump = false; // Disable double jump until grounded again
        }
    }

    public void SetAnimations()
    {
        if (moveX != 0 && isGroundedBool)
        {
            playeranim.SetBool("run", true);
            footEmissions.rateOverTime = 35f;
        }
        else
        {
            playeranim.SetBool("run", false);
            footEmissions.rateOverTime = 0f;
        }

        if (animHasIsGrounded)
        {
            playeranim.SetBool("isGrounded", isGroundedBool);
        }
    }

    private void FlipSprite(float direction)
    {
        if (direction > 0)
        {
            // Moving right, flip sprite to the right
            transform.localScale = new Vector3(1, 1, 1);
        }
        else if (direction < 0)
        {
            // Moving left, flip sprite to the left
            transform.localScale = new Vector3(-1, 1, 1);
        }
    }

    private void FixedUpdate()
    {
        // Player movement
        rb.linearVelocity = new Vector2(moveX * moveSpeed, rb.linearVelocity.y);
    }

    private void Jump(float jumpForce)
    {
        rb.linearVelocity = new Vector2(rb.linearVelocity.x, 0); // Zero out vertical velocity
        rb.AddForce(Vector2.up * jumpForce, ForceMode2D.Impulse);
        playeranim.SetTrigger("jump");
    }

    // R-PLT-09 (DEC-LAB-015): el rayo original nacía dentro del propio collider del jugador y
    // siempre detectaba "suelo" (salto infinito). Ahora se ignoran el jugador y los triggers (monedas).
    private readonly RaycastHit2D[] groundHits = new RaycastHit2D[4];

    public bool IsGrounded()
    {
        float rayLength = 0.25f;
        Vector2 rayOrigin = new Vector2(groundCheck.transform.position.x, groundCheck.transform.position.y - 0.1f);
        var filter = new ContactFilter2D { useTriggers = false };
        filter.SetLayerMask(groundLayer);
        int count = Physics2D.Raycast(rayOrigin, Vector2.down, filter, groundHits, rayLength);
        for (int i = 0; i < count; i++)
        {
            if (groundHits[i].collider.attachedRigidbody != rb)
            {
                return true;
            }
        }
        return false;
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "killzone")
        {
            GameManager.instance.Death();
        }
    }

    private static bool HasParameter(Animator animator, string name)
    {
        foreach (AnimatorControllerParameter p in animator.parameters)
        {
            if (p.name == name)
            {
                return true;
            }
        }
        return false;
    }
}
