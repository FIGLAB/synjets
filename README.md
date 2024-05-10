# Expressive, Scalable, Mid-air Haptics with Synthetic Jets

Open source code for <a href="https://dl.acm.org/doi/10.1145/3635150"> Expressive, Scalable, Mid-air Haptics with Synthetic Jets </a>.
This paper was published in the ACM Transactions on Computer-Human Interaction in January 2024. The paper will be presented at CHI 2024.
Contact me with questions <a href="vivian-shen.com">here</a>!

##### Note that the instructables is still in progress!
### Repository Contents
 - Demo Code has code used for a few of the demos with moving parts, i.e. steering wheel servos, unity code used for the HMD demo, etc.
 - Demo Stimuli has audacity files with the stimuli wavs for each application
 - Design Files contain all the laser cut files used for the applications
 - Stimuli Eliciation Study contains the stimuli used for the elicitation study
 - Stimuli Recognition Study contains all the stimuli used for the recognition study, as well as the python files used to automate the study.

### Assembly Instructions

The BoM is in the repository - these are just the materials we use, but synjets can be built with many different speakers, for a wide variety of devices!

Here is a brief summary of the assembly instructions. We will also have an instructables out very soon.
1) Choose the speaker you are using. Roughly, the larger the speaker, the farther/stronger the range of the synjet.
2) Fabricate the enclosure. I have included all the design files compatible with the speakers we've used - if you are using our tiniest speaker, we just cut a small hole out of cardstock and glued that on top.
3) If using the small class D amplifier, you can power it either through a 5V USB connection from your computer, or a 9-12V power adapter. Either way, strip one end of the cable and attach power to VCC and ground to GND on the amplifier.
![image](https://github.com/FIGLAB/synjets/assets/8129002/23a8b25d-f7d2-4656-97f0-5d614127991d)
4) Attach wires to the two terminals of your speaker, and then wire them to R+ and R- (or L+ and L-). The polarity doesn't really matter.
5) Plug in the USB power and an audio cable to your computer.
6) Play an appropriate sine wave through Audacity or any other audio software (you can find demo WAV files in stimuli recognition study).
7) Slowly turn the knob up. If everything went right you should be able to feel a stream!
![image](https://github.com/FIGLAB/synjets/assets/8129002/1b0b3c49-e4e2-443b-a549-340866c46fcc)




## License

This work is licensed under a GPL v 2.0 License file present in the repo. Please contact innovation@cmu.edu if you would like another license for your use.

## Reference

Vivian Shen, Chris Harrison, and Craig Shultz. 2024. Expressive, Scalable, Mid-air Haptics with Synthetic Jets. ACM Trans. Comput.-Hum. Interact. 31, 2, Article 14 (April 2024), 28 pages. https://doi.org/10.1145/3635150

BibTex Reference:
```
@article{10.1145/3635150,
author = {Shen, Vivian and Harrison, Chris and Shultz, Craig},
title = {Expressive, Scalable, Mid-air Haptics with Synthetic Jets},
year = {2024},
issue_date = {April 2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {31},
number = {2},
issn = {1073-0516},
url = {https://doi.org/10.1145/3635150},
doi = {10.1145/3635150},
abstract = {Non-contact, mid-air haptic devices have been utilized for a wide variety of experiences, including those in extended reality, public displays, medical, and automotive domains. In this work, we explore the use of synthetic jets as a promising and under-explored mid-air haptic feedback method. We show how synthetic jets can scale from compact, low-powered devices, all the way to large, long-range, and steerable devices (Figure&nbsp;1). We built seven functional prototypes targeting different application domains to illustrate the broad applicability of our approach. These example devices are capable of rendering complex haptic effects, varying in both time and space. We quantify the physical performance of our designs using spatial pressure and wind flow measurements and validate their compelling effect on users with stimuli recognition and qualitative studies.},
journal = {ACM Trans. Comput.-Hum. Interact.},
month = {jan},
articleno = {14},
numpages = {28},
keywords = {Non-contact haptics, mid-air haptics, synthetic jets}
}
```
