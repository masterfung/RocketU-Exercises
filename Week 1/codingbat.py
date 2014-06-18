__author__ = 'Johnny Hung'
#warmup1

def sleep_in(weekday,vacation):
	if weekday == False and vacation == False:
		return True
	elif weekday == True and vacation == False:
		return False
	else:
		return True


sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)

def monkey_trouble(a_smile, b_smile):
	if a_smile == True and b_smile == True:
		return True
	elif a_smile == False and b_smile == False:
		return True
	else:
		return False

def sum_double(a, b):
	if a == b:
		return (a + b)*2
	else:
		return a+b



def parrot_trouble(talking, hour):
	if talking == True and hour < 7:
		return True
	elif talking == True and hour == 7:
		return False
	elif talking == False and hour <=23:
		return False
	elif talking == True and hour > 20:
		return True
	elif talking == True and hour == 20:
		return False

def makes10(a, b):
	if a == 10 or b == 10:
		return True
	if (a + b) == 10:
		return True
	else:
		return False

def near_hundred(n):
	if n <= 100 and abs(100-n) <= 10:
		return True
	elif n > 100 and n < 200 and abs(100-n) <= 10:
		return True
	elif n <= 200 and abs(n-200) <=10:
		return True
	elif n > 200 and abs(n-200) <=10:
		return True
	else:
		return False

def pos_neg(a, b, negative):
	if a > 0 and b < 0 and negative == False:
		return True
	elif a < 0 and b > 0 and negative == False:
		return  True
	elif a < 0 and b < 0 and negative == True:
		return True
	else:
		return False

def not_string(str):
	if len(str) >= 3 and str[:3] == "not":
		return str
	return "not " + str
# str[:3] goes from the start of the string up to but not
# including index 3

def missing_char(str, n):
	start = str[:n]
	end = str[n+1:]
	return start + end

def front_back(str):
	if len(str) <= 1:
		return str
	mid = str[1:-1]  # can be written as str[1:len(str)-1]

	# last + mid + first
	return str[len(str)-1] + mid + str[0]


def front3(str):
	return str[0:3] * 3

def string_times(str, n):
	return str * n

def front_times(str, n):
	return str[:3] * n

def string_bits(str): # ***
	result = ''
	for i in range(len(str)):
		if i % 2 == 0:
			result = result + str[i]
	return result

def string_splosion(str):
	if len(str) < 2:
		return str
	if len(str) == 2:
		return str[0]*2 + str[1:2]
	if len(str) < 4 and len(str) > 2:
		return str[0]*2 + str[1] + str
	if len(str) < 5 and len(str) > 3:
		return str[0]*2 + str[1] + str[:3] + str
	if len(str) == 5:
		return str[0]*2 + str[1] + str[:3] + str[:4] + str
	if len(str) > 5:
		return str[0]*2 + str[1] + str[:3]+ str[:4] + str[:5] + str
	return str

def last2(str):
	count = 0
	if len(str) < 2:
		return 0
	last2 = str[-2]
	for i in range(len(str)-2):
		sub = str[i:i+2]
		if sub == last2:
			count += 1
	return count


def array_count9(nums):
	count = 0
	for i in nums:
		if i == 9:
			count +=1
	return count

def array_front9(nums):
	great = nums[:3]
	count = 0
	for i in great:
		if i == 9:
			count +=1
	if count > 0:
		return True
	else:
		return False

def array123(nums):
	count1 = 0
	count2 = 0
	count3 = 0
	for i in nums:
		if i == 1:
			count1 += 1
		if i == 2:
			count2 += 1
		if i == 3:
			count3 += 1
	if count1 >=1 and count2 >=1 and count3 >=1:
		return True
	else:
		return False

def string_match(a, b): #***
	shorter = min(len(a), len(b))
	count = 0

	for i in range(shorter-1):
		a_comp = a[i:i+1]
		b_comp = b[i:i+1]
		if a_comp == b_comp:
			count += 1
	return count

#string

def hello_name(name):
	return 'Hello '+ name + '!'

def make_abba(a, b):
  return a+b+b+a

def make_tags(tag, word):
	return '<' + tag + '>' + word + '</' + tag +'>'

def make_out_word(out, word):
	first = out[0:2]
	last = out[2:]
	return first + word + last

def extra_end(str):
	last_two = str[-2:]
	return last_two*3

def first_two(str):
	if len(str) <=2:
		return str
	else:
		return str[0:2]

def first_half(str):
	count = len(str)
	final = count/2
	return str[:final]

def without_end(str):
	first = str[1:len(str)-1]
	return first

def combo_string(a, b):
	if len(a) < len(b):
		return a+b+a
	else:
		return b+a+b

def non_start(a, b):
	chomp1 = a[1:]
	chomp2 = b[1:]
	return chomp1+chomp2

def left2(str):
	last = str[0:2]
	first = str[2:]
	if len(str) <=2:
		return str
	else:
		return first+last

#list1

def first_last6(nums):
	count = 0
	first = nums[0]
	last = nums[len(nums)-1]
	if first == 6:
		count += 1
	elif last == 6:
		count += 1
	if count >= 1:
		return True
	else:
		return False

def same_first_last(nums):

	return len(nums) > 0 and nums[0] == nums[-1]

def make_pi():
	return [3,1,4]

def common_end(a, b):
	return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
	return nums[0]+nums[1]+nums[2]

def sum2(nums):
	return sum(nums[:2])

def reverse3(nums):
	return [nums[2], nums[1], nums[0]]

def rotate_left3(nums):
	return [nums[1], nums[2], nums[0]]

def max_end3(nums):

	return [nums[0]]*3 if nums[0] >= nums[-1] else [nums[-1]]*3

#logic1
def cigar_party(cigars, is_weekend):
	if is_weekend == False and cigars <= 60 and cigars < 40:
		return False
	elif is_weekend == False and cigars >= 40 and cigars < 60:
		return True
	elif is_weekend == True and cigars >= 40:
		return True
	elif is_weekend == False and cigars <= 40:
		return False
	elif is_weekend == True and cigars < 40:
		return False
	elif is_weekend == False and cigars > 60:
		return False
	elif is_weekend == False and cigars == 60:
		return True

def date_fashion(you, date):
	if you <=2 or date <= 2:
		return 0

	if (you > 8 and you > 2) or (date > 8 and date > 2):
		return 2
	else:
		return 1

def squirrel_play(temp, is_summer):
	if temp > 60 and temp <= 90 and is_summer == False:
		return True
	if temp < 60 and is_summer == False:
		return False
	if temp > 90 and is_summer == False:
		return False
	if temp <= 100 and temp > 60 and is_summer == True:
		return True
	if temp < 60 and is_summer == True:
		return False
	if temp > 100 and is_summer == True:
		return False
	if temp == 60 and is_summer == False:
		return True
	else:
		return True

def caught_speeding(speed, is_birthday): #incomplete
	if speed <= 60 and is_birthday == False:
		return 0
	elif 61 <= speed <= 80 and is_birthday == False:
		return 1
	elif speed <= 65 and is_birthday == True:
		return 0
	elif speed >= 81 and is_birthday == False:
		return 2
	elif speed > 65 and is_birthday == False:
		return 2
	elif speed > 65 and is_birthday == True:
		return 1
	elif speed >= 81 and is_birthday == True:
		return 1
	else:
		return 2

def near_ten(num):
	if num % 10 <= 2:
		return True
	elif num % 10 >= 8:
		return True
	else:
		return False

def in1to10(n, outside_mode):
	if outside_mode == False and n > 10:
		return False
	if outside_mode == False and n == 10:
		return True
	elif outside_mode == False and n <=10 and n>=1:
		return True
	elif outside_mode == True and n>=10:
		return True
	elif outside_mode == True and n<= 1:
		return True
	else:
		return False

def love6(a, b):
	if a == 6 or b == 6:
		return True
	if (a+b) == 6:
		return True
	if abs(a-b) == 6:
		return True
	else:
		return False

def alarm_clock(day, vacation):
	wkd = '7:00'
	wnd = '10:00'
	if vacation == False and 1<= day <=5:
		return wkd
	elif vacation == False and (day == 6 or day == 0):
		return wnd
	elif vacation == True and 1<= day <=5:
		return wnd
	elif vacation == True and (day == 6 or day == 0):
		return 'off'
	else:
		return wkd

def sorta_sum(a, b):
	pass

#string2
def cat_dog(str):
	count

# list2

def count_evens(nums):
	count = 0
	for i in nums:
		if i % 2 == 0 or i == 0:
			count += 1
	return count

def big_diff(nums):
	return max(nums) - min(nums)