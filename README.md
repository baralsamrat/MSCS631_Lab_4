# MSCS631_Lab_4
Samrat Baral

Lab 4

University of the Cumberlands

2025 Spring - Advanced Computer Networks (MSCS-631-M40) - Full Term
Dr. Yousef Nijim

March 1, 2025

Understanding of Internet Control Message Protocol (ICMP). You will learn to implement a Ping application using ICMP request and reply to messages. See the attached document for full lab instructions.

# Screenshot
![1](/screenshots/Capture-1.PNG)
![2](/screenshots/Capture-2.PNG)
![3](/screenshots/Capture-3.PNG)

# Ouput 
```bash
chmod +x main.sh
```

```bash
./main.sh 
Pinging facebook.com .. *** START **** Test 
Pinging 157.240.19.35 using Python:

0.02026987075805664
0.016759395599365234
0.014838218688964844
0.018776416778564453
0.014089584350585938
0.014574527740478516
0.018991708755493164
0.01112675666809082
0.014893770217895508
0.014634370803833008
Pinging facebook.com .. *** COMPLETE **** Test
Pinging google.com (North America)...
Output for google.com saved in output_google.txt
Pinging bbc.co.uk (Europe)...
Output for bbc.co.uk saved in output_bbc.txt
Pinging baidu.com (Asia)...
Output for baidu.com saved in output_baidu.txt
Pinging uol.com.br (South America)...
Output for uol.com.br saved in output_uol.txt
All pings completed.
```

Files
- North America
[Google](src/output_google.txt)
```bash
Pinging 142.251.186.138 using Python:

0.02805781364440918
0.026309967041015625
0.038422584533691406
0.03463625907897949
0.08227133750915527
0.027217388153076172
0.025109529495239258
0.032682180404663086
0.029695510864257812
0.03139305114746094
```
- Europe
[BBC](src/output_bbc.txt)
```bash
Pinging 151.101.192.81 using Python:

0.01801609992980957
0.015864849090576172
0.011957645416259766
0.01675105094909668
0.018955707550048828
0.021721363067626953
0.018233299255371094
0.01292276382446289
0.019211769104003906
0.01407003402709961
```
- Asia
[Baidu](src/output_baidu.txt)
```bash
Pinging 39.156.66.10 using Python:

0.2580113410949707
0.24934816360473633
0.250171422958374
0.25200438499450684
0.2508993148803711
0.25026774406433105
0.24828314781188965
0.26306986808776855
```
- South America
[UOL](src/output_uol.txt)
```bash
Pinging 200.147.35.149 using Python:

0.17101669311523438
0.16144275665283203
0.1620163917541504
0.179443359375
0.1618025302886963
0.16349220275878906
0.1607060432434082
0.17411088943481445
0.16693496704101562
```
# Experience and Challenges:
- Working on this lab assignment was a challenging yet rewarding experience. Implementing a custom Ping application using ICMP in Python pushed me to explore low-level network programming and raw sockets. One of the initial challenges I encountered was dealing with Python 3's handling of bytes, particularly with the checksum function. The error caused by using the ord() function on bytes required me to adapt the code, which deepened my understanding of how Python 3 differs from earlier versions. Debugging this issue and ensuring that the ICMP packet headers were correctly structured helped solidify my grasp on network protocols and the nuances of Python's binary data handling.

- Integrating the Python code with a shell script to generate output files for different target hosts across continents was another significant challenge. Running the scripts in a Windows environment using Git Bash required me to adjust command aliases (switching from python3 to py -3) and manage output flushing so that results were saved correctly when the script was terminated by a timeout. Despite these hurdles, the process was invaluable in teaching me cross-platform scripting and troubleshooting in mixed operating environments. Overall, this lab enhanced my technical skills and provided a practical insight into the implementation and debugging of network applications.

