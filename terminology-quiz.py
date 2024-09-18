import random

print("Welcome to AWS re/Start Terminology quiz")

player = input('Do you want to play? (yes/no) ')

if player.lower() != 'yes':
      quit()

print("Okay! Let's play :)")


quiz_questions = [
    ("What does CPU stand for?", "central processing unit"),
    ("What does GPU stand for?", "graphics processing unit"),
    ("What does RAM stand for?", "random access memory"),
    ("What does SSD stand for?", "solid state drive"),
    ("What does Nmap stand for?", "network mapper"),
    ("What does ICMP stand for?", "internet control message protocol"),
    ("What does SNMP stand for?", "simple network management protocol"),
    ("What does NAT stand for?", "network address translation"),
    ("What does IPS stand for?", "intrusion prevention system"),
    ("What does CIDR stand for?", "classless inter-domain"),
    ("What does NIC stand for?", "network interface card "),
    ("What does AWS stand for?", "amazon web services"),
    ("What does RDS in AWS  stand for?", "relational database service"),
    ("What does S3  in AWS  stand for?", "simple storage service"),
    ("What does EC2 in AWS  stand for?", "elastic compute cloud"),
    ("What does ECS in AWS  stand for?", "elastic container service"),
    ("What does EKS in AWS  stand for?", "elastic kubernetes service"),
    ("What does VPC in AWS  stand for?", "virtual private cloud"),
    ("What does ELB in AWS  stand for?", "elastic load balancing"),
    ("What does IAM in AWS  stand for?", "identity and access management"),
    ("What does SNS in AWS  stand for?", "simple notification service"),
    ("What does ELB in AWS  stand for?", "elastic load balancing"),
    ("What does Route 53 in AWS  stand for?", "dns web service"),
    ("What does KMS in AWS  stand for?", "key management service"),
    ("What does DynamoDB in AWS  stand for?", "noSQL database service"),
    ("What does CloudWatch in AWS  stand for?", "monitoring and logging service"),
    ("What does HTTP stand for?", "hypertext transfer protocol"),
    ("What does HDD stand for?", "hard disk drive")
]

random.shuffle(quiz_questions)
selected_questions = quiz_questions[:5]

score = 0 

for question, correct_answer in selected_questions:
      answer = input(question + " ")
      if answer.lower() == correct_answer:
            print ('Correct answer!  :)')
            score += 1
      else:
            print('Incorrect!! :(')

print('You got ' + str(score) + ' questions correct! :)' )
print("Your Score is " + str((score / 5) * 100) + "%.")