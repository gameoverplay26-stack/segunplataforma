using UnityEngine;

// Enemigo del nivel 2: va y viene entre dos puntos en X. Tiene la etiqueta "killzone",
// así que el PlayerController ya existente lo trata como un peligro al chocar.
[RequireComponent(typeof(Rigidbody2D))]
public class PatrolEnemy : MonoBehaviour
{
    public float minX;
    public float maxX;
    public float speed = 2.5f;

    private Rigidbody2D rb;
    private int direction = 1;

    private void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
        rb.bodyType = RigidbodyType2D.Kinematic;
    }

    private void FixedUpdate()
    {
        Vector2 p = rb.position;
        if (p.x >= maxX) direction = -1;
        else if (p.x <= minX) direction = 1;

        p.x += direction * speed * Time.fixedDeltaTime;
        rb.MovePosition(p);

        Vector3 s = transform.localScale;
        s.x = Mathf.Abs(s.x) * (direction > 0 ? 1 : -1);
        transform.localScale = s;
    }
}
