using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class start_splash : MonoBehaviour
{
    public ParticleSystem system;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter(Collider other)
    {
        system.Play();
    }

    private void OnTriggerExit(Collider other)
    {
        Destroy(system);
        system.Pause();
    }
}
