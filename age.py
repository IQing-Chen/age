driving = input('請問有沒有開過車？')
if driving != '有' and driving !='沒有':
	print('輸入錯誤，只能輸入有/沒有')
	raise SystemExit	#讓程式終止

age = int(input('請問年齡？'))
if driving == '有':
	if age >= 18:
		print('通過測驗')
	else:
		print('違法了')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照')
	else:
		print('還不能考駕照')