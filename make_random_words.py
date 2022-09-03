import random, string

def make_header_str (str):
  return "#" * len(str) + "\n" + str + "\n" + "#" * len(str) + "\n"

## 最初の文字を出力する関数
def view_start_screen ():
  print(make_header_str("ランダムな文字列を作成するツール"))

## タイプが文字列(type = "string")なら、condition_arrayに含まれる文字があるまで、
## タイプが数値(type = "number")なら、condition_arrayに含まれる最小値(condition_array[0])と最大値(condition_array[1])が出るまで
## 入力を繰り返す関数。
def view_input_menu (type, condition_array, input_text, error_message = "正しく入力してください。"):
  while True:
    ans = input(input_text)
    if type == "string" and ans in condition_array:
      return ans
    elif ans.isdigit() and type == "number" and int(ans) >= condition_array[0] and int(ans) <= condition_array[1]:
      return int(ans)
    else:
      print(error_message)


## モードをチェックし、論理値型で戻す
def choice_make_mode():
  result_array = {}
  mode_array = [
    {
      "type": "useNumber",
      "words": "数を使用する"
    },
    {
      "type": "useSymbol",
      "words": "記号を使用する"
    }
  ]
  for content in mode_array:
    result_array[content["type"]] = "y" == view_input_menu("string", ["y", "n"], content["words"] + "=>")
  return result_array

## モードに合わせてlength分の文字列を作成する関数
def make_random_words (mode_array, length):
  target_string = string.ascii_letters
  if mode_array["useNumber"]:
    target_string += string.digits
  if mode_array["useSymbol"]:
    target_string += string.punctuation
  randlst = [random.choice(target_string) for i in range(length)]
  return ''.join(randlst)

## メイン
def main ():
  view_start_screen()
  while True:
    print(make_random_words(choice_make_mode(), view_input_menu("number", [1, 100], "長さ" + "=>")))
    if "n" == view_input_menu("string", ["y", "n"], "もう一度しますか" + "=>"):
      break

main()