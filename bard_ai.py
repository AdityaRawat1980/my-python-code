from bardapi import Bard
import os

os.environ["_BARD_API_KEY"]="g.a000iQiD2eip_SRvwJDHm0dK16GQN_ea7WyU0FW_i7qNUxhyfgfG7dPz9gT4ddr3MvQnwEz-qAACgYKARYSAQASFQHGX2MiV23Xx9_WclD6RkolR7aMfhoVAUF8yKqpJfgOSI03fos4tj7vhLH80076"
qurry =input("enter you qurry :- ")
print(Bard().get_answer(str(qurry)))
