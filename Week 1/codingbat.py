__author__ = 'Johnny Hung'
# warmup1

# ones with three *** needs to be reviewed again.

def sleep_in(weekday, vacation):
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
		return (a + b) * 2
	else:
		return a + b


def parrot_trouble(talking, hour):
	if talking == True and hour < 7:
		return True
	elif talking == True and hour == 7:
		return False
	elif talking == False and hour <= 23:
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
	if n <= 100 and abs(100 - n) <= 10:
		return True
	elif n > 100 and n < 200 and abs(100 - n) <= 10:
		return True
	elif n <= 200 and abs(n - 200) <= 10:
		return True
	elif n > 200 and abs(n - 200) <= 10:
		return True
	else:
		return False


def pos_neg(a, b, negative):
	if a > 0 and b < 0 and negative == False:
		return True
	elif a < 0 and b > 0 and negative == False:
		return True
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
	end = str[n + 1:]
	return start + end


def front_back(str):
	if len(str) <= 1:
		return str
	mid = str[1:-1]  # can be written as str[1:len(str)-1]

	# last + mid + first
	return str[len(str) - 1] + mid + str[0]


def front3(str):
	return str[0:3] * 3


def string_times(str, n):
	return str * n


def front_times(str, n):
	return str[:3] * n


def string_bits(str):  # ***
	result = ''
	for i in range(len(str)):
		if i % 2 == 0:
			result = result + str[i]
	return result


def string_splosion(str):
	if len(str) < 2:
		return str
	if len(str) == 2:
		return str[0] * 2 + str[1:2]
	if len(str) < 4 and len(str) > 2:
		return str[0] * 2 + str[1] + str
	if len(str) < 5 and len(str) > 3:
		return str[0] * 2 + str[1] + str[:3] + str
	if len(str) == 5:
		return str[0] * 2 + str[1] + str[:3] + str[:4] + str
	if len(str) > 5:
		return str[0] * 2 + str[1] + str[:3] + str[:4] + str[:5] + str
	return str


def last2(str):
	count = 0
	if len(str) < 2:
		return 0
	last2 = str[-2]
	for i in range(len(str) - 2):
		sub = str[i:i + 2]
		if sub == last2:
			count += 1
	return count


def array_count9(nums):
	count = 0
	for i in nums:
		if i == 9:
			count += 1
	return count


def array_front9(nums):
	great = nums[:3]
	count = 0
	for i in great:
		if i == 9:
			count += 1
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
	if count1 >= 1 and count2 >= 1 and count3 >= 1:
		return True
	else:
		return False


def string_match(a, b):  #***
	shorter = min(len(a), len(b))
	count = 0

	for i in range(shorter - 1):
		a_comp = a[i:i + 1]
		b_comp = b[i:i + 1]
		if a_comp == b_comp:
			count += 1
	return count


#string

def hello_name(name):
	return 'Hello ' + name + '!'


def make_abba(a, b):
	return a + b + b + a


def make_tags(tag, word):
	return '<' + tag + '>' + word + '</' + tag + '>'


def make_out_word(out, word):
	first = out[0:2]
	last = out[2:]
	return first + word + last


def extra_end(str):
	last_two = str[-2:]
	return last_two * 3


def first_two(str):
	if len(str) <= 2:
		return str
	else:
		return str[0:2]


def first_half(str):
	count = len(str)
	final = count / 2
	return str[:final]


def without_end(str):
	first = str[1:len(str) - 1]
	return first


def combo_string(a, b):
	if len(a) < len(b):
		return a + b + a
	else:
		return b + a + b


def non_start(a, b):
	chomp1 = a[1:]
	chomp2 = b[1:]
	return chomp1 + chomp2


def left2(str):
	last = str[0:2]
	first = str[2:]
	if len(str) <= 2:
		return str
	else:
		return first + last


#list1

def first_last6(nums):
	count = 0
	first = nums[0]
	last = nums[len(nums) - 1]
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
	return [3, 1, 4]


def common_end(a, b):
	return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
	return nums[0] + nums[1] + nums[2]


def sum2(nums):
	return sum(nums[:2])


def reverse3(nums):
	return [nums[2], nums[1], nums[0]]


def rotate_left3(nums):
	return [nums[1], nums[2], nums[0]]


def max_end3(nums):
	return [nums[0]] * 3 if nums[0] >= nums[-1] else [nums[-1]] * 3


def middle_way(a, b):
	return [a[1], b[1]]


def make_ends(nums):
	return [nums[0], nums[-1]]


def has23(nums):
	count = 0
	for i in nums:
		if i == 3:
			count += 1
		elif i == 2:
			count += 1
	if count > 0:
		return True
	else:
		return False


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
	if you <= 2 or date <= 2:
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


def caught_speeding(speed, is_birthday):
	speeding = speed - (65 if is_birthday else 60)
	if speeding > 20:
		return 2
	elif speeding > 0:
		return 1
	else:
		return 0


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
	elif outside_mode == False and n <= 10 and n >= 1:
		return True
	elif outside_mode == True and n >= 10:
		return True
	elif outside_mode == True and n <= 1:
		return True
	else:
		return False


def love6(a, b):
	if a == 6 or b == 6:
		return True
	if (a + b) == 6:
		return True
	if abs(a - b) == 6:
		return True
	else:
		return False


def alarm_clock(day, vacation):
	wkd = '7:00'
	wnd = '10:00'
	if vacation == False and 1 <= day <= 5:
		return wkd
	elif vacation == False and (day == 6 or day == 0):
		return wnd
	elif vacation == True and 1 <= day <= 5:
		return wnd
	elif vacation == True and (day == 6 or day == 0):
		return 'off'
	else:
		return wkd


def sorta_sum(a, b):
	sum = a + b
	if 10 <= sum <= 19:
		return 20
	else:
		return sum


#string2

def cat_dog(str):
	return str.count('cat') == str.count('dog')


def double_char(str):
	new_word = ''
	for i in str:
		new_word += i * 2
	return new_word


def count_hi(str):
	return str.count('hi')


def count_code(str):
	count = 0
	return str.count('code') + str.count('cope') + str.count('cooe') + str.count('coze') + str.count(
		'core') + str.count('cole')


def end_other(a, b):  #***
	a = a.lower()
	b = b.lower()
	long_s, short_s = (a, b) if len(a) >= len(b) else (b, a)
	return long_s.endswith(short_s)


def xyz_there(str):  # ***
	i = 0
	while "xyz" in str[i:]:
		if str[i - 1 + str[i:].index("xyz")] != ".":
			return True
		i += str[i:].index("xyz") + 2
	return False


# period = 0
# i = 0
# if len(str) > 3:
# 	if str.count('.') == True:
# 		period += 1
# 	elif str.count('xyz'):
# 		i += 1
# 	if period > 0:
# 		return False
# 	elif i > 0:
# 		return True
# else:
# 	return False


# list2

def count_evens(nums):
	count = 0
	for i in nums:
		if i % 2 == 0 or i == 0:
			count += 1
	return count


def big_diff(nums):
	return max(nums) - min(nums)


def sum67(nums):  #***
	for i in range(0, len(nums)):
		if nums[i] == 6:
			nums[i] = 0
			for j in range(i + 1, len(nums)):
				temp = nums[j]
				nums[j] = 0
				if temp == 7:
					i = j + 1
					break
	return sum(nums)


def centered_average(nums):
	sum = 0
	for i in nums:
		sum += i
	return (sum - (max(nums) + min(nums))) / (len(nums) - 2)


def sum13(nums):
	if len(nums) == 0:
		return 0
	for i in range(0, len(nums)):
		if nums[i] == 13:
			nums[i] = 0
			if i + 1 < len(nums):
				nums[i + 1] = 0
	return sum(nums)


def has22(nums): #***
	for i in range(0, len(nums)-1):
		if nums[i] == 2 and nums[i+1] == 2:
			return True
	else:
		return False

#logic 2

def make_bricks(small, big, goal):
	sum = goal
	sum -= 5 * min(big, goal / 5)
	return sum - small <= 0


def lone_sum(a, b, c):
	sum = 0
	if a == b == c:
		sum = 0
		return sum
	elif a == c:
		sum = b
		return sum
	elif b == c:
		sum = a
		return sum
	elif a == b:
		sum = c
		return sum
	else:
		sum = a + b + c
		return sum


def lucky_sum(a, b, c):
	sum = 0
	if a == 13:
		return sum
	elif b == 13:
		sum = a
		return sum
	elif c == 13:
		sum = a + b
		return sum
	else:
		sum = a + b + c
		return sum


def no_teen_sum(a, b, c):  # ***
	def fix_teen(n):
		return n if n not in [13, 14, 17, 18, 19] else 0

	return fix_teen(a) + fix_teen(b) + fix_teen(c)


def round_sum(a, b, c):
	def round10(num):
		return (num + 5) / 10 * 10

	return round10(a) + round10(b) + round10(c)


def close_far(a, b, c):  #***
	return (abs(abs(b) - abs(c)) >= 2) and \
		   ((abs(abs(b) - abs(a)) <= 1 and abs(abs(c) - abs(a)) >= 2) \
			or (abs(abs(c) - abs(a)) <= 1 and abs(abs(b) - abs(a)) >= 2))


def make_chocolate(small, big, goal):
	sum = goal
	sum -= 5 * min(big, goal / 5)
	if sum > small:
		return -1
	else:
		return sum