using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class car_move : MonoBehaviour
{
    bool moving = false;
    Rigidbody m_Rigidbody;
    float m_Speed;

    // Start is called before the first frame update
    void Start()
    {
        m_Rigidbody = GetComponent<Rigidbody>();
        //Set the speed of the GameObject
        m_Speed = 2.0f;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("space") && !moving)
        {
            moving = true;
            m_Rigidbody.velocity = transform.forward * m_Speed;
        }
        if (moving)
        {
            this.transform.position += transform.forward * 0.00005f;
        }

    }
}
