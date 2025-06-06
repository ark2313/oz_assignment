{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제1. oz라는 폴더가 있다는 가정하에 oz 폴더의 위치를 찾는 명령어를 작성해주세요"

Which oz



   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제2. 문제 2: 2024년 5월의 달력을 화면에 보여주는 리눅스 명령어를 작성해주세요"


Cal 5 2024


   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제 3: echo 명령어를 이용해 oz.txt라는 파일을 생성하고 파일안에 “Hello Linux”라는 내용이 들어갈 수 있도록 리눅스 명령어를 작성해주세요"



 echo "Hello Linux" 1> oz.txt




   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제 4 : 다음과 같은 명령어가 주어졌을 때, 그 결과로 무엇이 기대되는지 맞춰보세요.\n",
    "\n",
    "```bash\n",
    "echo \"apple banana orange\" | xargs -n 1 echo\n",
    "```"


Apple

Banana

Orange




   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제 5: 아래와 같은 순서로 명령어가 입력 되었을때 4번째 명령어를 다시 사용하기 위한 리눅스 명령어를 작성해주세요\n",
    "\n",
    "1. echo oz\n",
    "2. Clear\n",
    "3. History\n",
    "4. Cal\n",
    "5. Clear\n",
    "6. which oz\n"

!4


   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제6. 아래 설명 중 틀린 내용을 모두 골라주세요\n",
    "\n",
    "1. CommandNames 들은 쉘의 검색 PATH 안에 있어야 합니다.\n",
    "2. 쉘은 터미널을 통해 명령이 제출될 때 명령의 의미를 해석하는 것입니다.\n",
    "3. Linux 명령은 CommandName -options input 구조를 따릅니다.\n",
    "4. 일부 명령에는 짧은 형식 옵션만 사용할 수 있습니다.\n",
    "5. 긴 형식 옵션에는 대시 1개 (-)가 있고 짧은 형식 옵션에는 대시 2개(--)가 있습니다."

1번



   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제7. Piping에 대한 설명으로 옳은것을 골라주세요\n",
    "\n",
    "1. 한 명령의 표준 출력을 다른 명령의 표준 입력에 연결하는 것이다\n",
    "2. 네트워크 연결 여부를 확인하는 명령어다\n",
    "3. 입력된 데이터를 모아 한번에 저장하기 위해 사용되는 명령어다\n",
    "4. 삭제된 파일 목록을 확인하기 위한 명령어다"


1번



   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제8. \"example.txt\" 파일에 \"Hello, world!\"라는 문자열을 기록하고, 동시에 터미널에도 출력하려고 합니다. 올바른 tee 명령어를 작성하세요."



echo "Hello, world!" | tee example.txt


   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제9. 파이프라인과 명령을 기억하기 쉬운 별명으로 저장하기 위해 사용하는 명령어를 골라주세요\n",
    "\n",
    "1. Aliases\n",
    "2. Set\n",
    "3. Reference\n",
    "4. TEE\n",
    "5. xargs"

1번


   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "문제10. 현재 디렉토리에 여러개의 `.txt` 파일이 있다고 가정해봅시다. 다른 파일은 남기고 `.txt`로 끝나는 파일들만 삭제하기 위해 작성해야 하는 명령어를 작성해보세요"








   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}