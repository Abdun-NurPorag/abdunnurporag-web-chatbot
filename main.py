print("\t\tWelcome., Hello I am 🧑‍💻 AI chatbot.")
print()
print("How can I help you. You can told me your question or ideas here. Porag will read it. He is not available in internet evertime.So he build this AI robot.This robot will take your question or anything else and it will be store on its memory.Then porag will read it.")
print("এটি একটি কৃতিম বুদ্ধি সম্পন্ন রোবট।যেহেতু পরাগ সবসময় আনলাইনে থাকে না তাই তার পরিবর্তে এটি কর্মক্ষম থাকে ২৪ ঘন্টা।যেকোন প্রশ্ন করলে এটি তা তার মমোরিতে সংরক্ষন করে থাকে। পরবর্তিতে আমি তা দেখতে পারি।")
print("____________")
print("-------------------------")
print(" রোবোটের ভাষা নির্বাচন করুন:\n1-Bangla এর জন্য B এন্টার করুন।\n2-English এর জন্য E এন্টর করুন। আর যদি কোন টি এন্টার না করেন তাহলে system  এর ভাষা চালু হবে।")
print("")
print("_____________________")
language=input("Language➤")
print("_____________________")
if language=="B":
	print("____________________")
	print("\t\tActive language:Bangla")
	print("\t\tAi verson:1.1")
	while True:
		print("----Starting------")
		print("এন্টার বাটন চাপুন➤")
		action=input()
		question_1=input("[আপনার প্রশ্ন]➤")
		email_1=input("[আপনার ই-মেইল]➤")
		if question_1=="" or email_1=="" or question_1 and email_1 =="":
			print("\t\t-------------------")
			print("\tদুঃখিত আপনার তথ্য সংরক্ষণ হয়নি করান আপনি ই-মেইল বা অন্যটি ফঁাকা রেখেছেন। পরবর্তিতে আবার চেষ্টা করুন।")
		else:
			print("\t\t🙂🙂🙂ধন্যবাদ আপনাকে")
			file_english="\n[\nEmail="+email_1+"\nQuestion="+"\n]"
			file_name="Bangla/bangla.txt"
			file_1=open(file_name,"a")
			file_1.write(file_english)
			file_1.close()

elif language=="E":
	print("____________________")
	print("\t\tActive Language:English")
	print("\t\tAi verson:1.1")
	while True:
		print("----Starting------")
		print("Press Enter butyon➤")
		action=input()
		question_1=input("[Your question]➤")
		email_1=input("[Your email]➤")
		if question_1=="" or email_1=="" or question_1 and email_1 =="":
			print("\t\t-------------------")
			print("\tData does not save because you do not enter proper information")
		else:
			print("\t\t🙂🙂🙂Thank you")
			file_english="\n[\nEmail="+email_1+"\nQuestion="+"\n]"
			file_name="English/english.txt"
			file_1=open(file_name,"a")
			file_1.write(file_english)
			file_1.close()
else:
	print("____________________")
	print("\t\tActive Language:English")
	print("\t\tAi verson:1.1")
	while True:
		print("----Starting------")
		print("Press Enter butyon➤")
		action=input()
		question_1=input("[Your question]➤")
		email_1=input("[Your email]➤")
		if question_1=="" or email_1=="" or question_1 and email_1 =="":
			print("\t\t-------------------")
			print("\tData does not save because you do not enter proper information")
		else:
			print("\t\t🙂🙂🙂Thank you")
			file_english="\n[\nEmail="+email_1+"\nQuestion="+"\n]"
			file_name="English/english.txt"
			file_1=open(file_name,"a")
			file_1.write(file_english)
			file_1.close()