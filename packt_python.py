{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.140000000000001"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# this is comment pi=3.14\n",
    "pi = 3.14\n",
    "pi + 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hipotenus_uzunlugu=  5.0\n"
     ]
    }
   ],
   "source": [
    "#pythogorean theorem\n",
    "import math\n",
    "x = 3\n",
    "y = 4\n",
    "z = math.sqrt(x**2 + y**2)\n",
    "print ('hipotenus_uzunlugu= ', z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "birinci_kenar_uzunlugu_gir = 6\n",
      "ikinci_kenar_uzunlugu_gir = 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " hipotenus = 10.0\n"
     ]
    }
   ],
   "source": [
    "x = input ('birinci_kenar_uzunlugu_gir =')\n",
    "y = input ('ikinci_kenar_uzunlugu_gir =')\n",
    "\n",
    "print ( ' hipotenus =', math.sqrt(float(x)**2 + float(y)**2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "bookstore = 'City Lights'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'City Lights'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bookstore"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " seni seviyorum lan Jale\n"
     ]
    }
   ],
   "source": [
    "x = ' seni seviyorum lan Jale'\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ahlan wa sahlan.\n"
     ]
    }
   ],
   "source": [
    "arabic_greeting = 'Ahlan wa sahlan.'\n",
    "print(arabic_greeting)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " seni seviyorum lan Jale\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola Senor.\n"
     ]
    }
   ],
   "source": [
    "spanish_greeting = 'Hola '\n",
    "print(spanish_greeting + 'Senor.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola  Senor.\n"
     ]
    }
   ],
   "source": [
    "spanish_greeting = 'Hola '\n",
    "print(spanish_greeting,'Senor.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HelloHelloHelloHelloHello\n"
     ]
    }
   ],
   "source": [
    "greeting = 'Hello'\n",
    "print(greeting * 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The founder of City Lights Bookstore, Lawrence Ferlinghetti , is now 1001 years old hasan.\n"
     ]
    }
   ],
   "source": [
    "owner = 'Lawrence Ferlinghetti'\n",
    "age = 1001\n",
    "name = 'hasan'\n",
    "print('The founder of City Lights Bookstore, {} , is now {} years old {}.'.format(owner, age, name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#tirnak icinde gireni saydi\n",
    "orhan_ari = 'datascientist'\n",
    "len('orhan_ari')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orhan_ari = 'datascientist'\n",
    "len(orhan_ari)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "name = 'orhan_ari'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ORHAN_ARI'"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'orhan_ari'"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Orhan_ari'"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.capitalize()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name = 'orhan_ari'\n",
    "name.count('a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# count buyuk kucuk harf duyarli olarak sayar\n",
    "name = 'orhAn_ari'\n",
    "name.count('a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "## w3r examples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## versiyon sorgulama"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python versiyonum: \n",
      "3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print ('python versiyonum: ')\n",
    "print(sys.version)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## tarih yazdirma"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2020-06-02 21:37:09\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "now = datetime.datetime.now()\n",
    "print(now.strftime(\"%Y-%m-%d %H:%M:%S\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Write a Python program which accepts the radius of a circle from the user and compute the area."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import math\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Alani hesaplanacak dairenin yaricapini giriniz = 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Yaricapi 2 olan dairenin alani = 12.566370614359172\n"
     ]
    }
   ],
   "source": [
    "r = input('Alani hesaplanacak dairenin yaricapini giriniz =')\n",
    "Alan = pi * float(r)**2\n",
    "print(' Yaricapi ' +str(r)+ ' olan dairenin alani =', str(Alan))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input the radius of the circle :  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of the circle with radius 2.0 is: 12.566370614359172\n"
     ]
    }
   ],
   "source": [
    "r = float(input (\"Input the radius of the circle : \"))\n",
    "print (\"The area of the circle with radius \" + str(r) + \" is: \" + str(pi * r**2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input first name: orhan\n",
      "Input last name: ari\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iranahro\n"
     ]
    }
   ],
   "source": [
    "x = input('Input first name:')\n",
    "y = input('Input last name:')\n",
    "z = (x + y)[::-1]\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input your First Name :  orhan\n",
      "Input your Last Name :  ari\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello  ari orhan\n"
     ]
    }
   ],
   "source": [
    "fname = input(\"Input your First Name : \")\n",
    "lname = input(\"Input your Last Name : \")\n",
    "print (\"Hello  \" + lname + \" \" + fname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input four number = 1234\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List :[1,2,3,4]\n",
      "Tuple2 :(1,2,3,4)\n"
     ]
    }
   ],
   "source": [
    "first,second,third,fourth = input('Input four number =')\n",
    "print('List :'+ '['+ str(first) + ','+  str(second) + ',' + str(third) + ',' + str(fourth) +  ']' )\n",
    "print('Tuple2 :'+ '('+ str(first) + ','+  str(second) + ',' + str(third) + ',' + str(fourth)  + ')' )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input some comma seprated numbers :  1,2,3,4\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'tuple' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-6030b101377c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Input some comma seprated numbers : \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mlist\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalues\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\",\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mtuple\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtuple\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'List : '\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Tuple : '\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtuple\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object is not callable"
     ]
    }
   ],
   "source": [
    "values = input(\"Input some comma seprated numbers : \")\n",
    "list = values.split(\",\")\n",
    "tuple = tuple(list)\n",
    "print('List : ',list)\n",
    "print('Tuple : ',tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " ## 7.Write a Python program to accept a filename from the user and print the extension of that."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input the filename: hasan.dat\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File extension:dat\n"
     ]
    }
   ],
   "source": [
    "x= input('Input the filename:')\n",
    "y = x.split('.')\n",
    "print('File extension:'+ y[-1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "##8. Write a Python program to display the first and last colors from the following list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First_color:Red Last_color:Black\n"
     ]
    }
   ],
   "source": [
    "color_list = [\"Red\",\"Green\",\"White\" ,\"Black\"]\n",
    "print('First_color:' + color_list[0] + ' Last_color:' + color_list[-1] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The examination will start from :11/12/2014\n"
     ]
    }
   ],
   "source": [
    "exam_st_date = (11, 12, 2014)\n",
    "print('The examination will start from :' + str(exam_st_date[0]) +'/' + str(exam_st_date[1]) + '/' + str(exam_st_date[2]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##EDITORUN COZUMU  % ile eleman secimi guzelmis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The examination will start from : 11 / 12 / 2014 \n"
     ]
    }
   ],
   "source": [
    "date = (11,12,2014)\n",
    "print( \"The examination will start from : %i / %i / %i \"%date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input n values =  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Value of n+nn+nnn = 615\n"
     ]
    }
   ],
   "source": [
    "n = input('Input n values = ')\n",
    "x = n+n\n",
    "y = n+n+n\n",
    "z = int(n)+int(x)+int(y)\n",
    "print('Value of n+nn+nnn = ' + str(z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##EDITORUN COZUMU "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = int(input(\"Input an integer : \"))\n",
    "n1 = int( \"%s\" % a )\n",
    "n2 = int( \"%s%s\" % (a,a) )\n",
    "n3 = int( \"%s%s%s\" % (a,a,a) )\n",
    "print (n1+n2+n3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "marcog 42\n"
     ]
    }
   ],
   "source": [
    "name = 'marcog'\n",
    "number = 42\n",
    "print ('%s %d' % (name, number))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "marcog 42\n"
     ]
    }
   ],
   "source": [
    "name = 'marcog'\n",
    "number = 42\n",
    "print(name, number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import math\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Return the absolute value of the argument.\n"
     ]
    }
   ],
   "source": [
    "print(abs.__doc__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mabs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m/\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m Return the absolute value of the argument.\n",
       "\u001b[1;31mType:\u001b[0m      builtin_function_or_method\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "?abs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " PRINT yerine FORMAT kullanimi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'one two'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{} {}'.format('one', 'two')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'      test'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{:>10}'.format('test')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'test      '"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{:10}'.format('test')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 12. Write a Python program to print the calendar of a given month and year."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "input the year : 2020\n",
      "input the month : 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     June 2020\n",
      "Mo Tu We Th Fr Sa Su\n",
      " 1  2  3  4  5  6  7\n",
      " 8  9 10 11 12 13 14\n",
      "15 16 17 18 19 20 21\n",
      "22 23 24 25 26 27 28\n",
      "29 30\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import calendar\n",
    "y = int(input('input the year :'))\n",
    "m = int(input('input the month :'))\n",
    "\n",
    "print(calendar.month(y, m))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## direk kalendar yazdirma"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      May 2020\n",
      "Mo Tu We Th Fr Sa Su\n",
      "             1  2  3\n",
      " 4  5  6  7  8  9 10\n",
      "11 12 13 14 15 16 17\n",
      "18 19 20 21 22 23 24\n",
      "25 26 27 28 29 30 31\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(calendar.month(2020, 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mType:\u001b[0m        module\n",
       "\u001b[1;31mString form:\u001b[0m <module 'calendar' from 'C:\\\\Users\\\\User\\\\anaconda3\\\\lib\\\\calendar.py'>\n",
       "\u001b[1;31mFile:\u001b[0m        c:\\users\\user\\anaconda3\\lib\\calendar.py\n",
       "\u001b[1;31mDocstring:\u001b[0m  \n",
       "Calendar printing functions\n",
       "\n",
       "Note when comparing these calendars to the ones printed by cal(1): By\n",
       "default, these calendars have Monday as the first day of the week, and\n",
       "Sunday as the last (the European convention). Use setfirstweekday() to\n",
       "set the first day of the week (0=Monday, 6=Sunday).\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "?calendar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##13. Write a Python program to print the following here document. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\" a string that you \"don't\" have to escape\n",
      "This \n",
      "is a ........ multi-line\n",
      "heredoc string---------> example\n"
     ]
    }
   ],
   "source": [
    "print(\"\"\"\" a string that you \"don't\" have to escape\n",
    "This \n",
    "is a ........ multi-line\n",
    "heredoc string---------> example\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "14. Write a Python program to calculate number of days between two dates."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "382\n"
     ]
    }
   ],
   "source": [
    "from datetime import date\n",
    "f_date = date(2014, 7, 2)\n",
    "l_date = date(2015, 7, 19)\n",
    "fark = l_date - f_date\n",
    "print(fark.days)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 15. Write a Python program to get the volume of a sphere with radius 6."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "volume of a sphere with radius 6 = 904.7786842338603\n"
     ]
    }
   ],
   "source": [
    "r = 6\n",
    "V = 4/3*(pi * r**3)\n",
    "print('volume of a sphere with radius 6 = ' + str(V))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input a number : 22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Difference = 10.0\n"
     ]
    }
   ],
   "source": [
    "x = float(input('Input a number :'))\n",
    "if x < 17:\n",
    "    print('Difference =' + str(17-x))\n",
    "else: \n",
    "    print ('Difference = ' + str(2*(x - 17)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "def difference(n):\n",
    "    if n <= 17:\n",
    "        return 17 - n\n",
    "    else:\n",
    "        return (n - 17) * 2 \n",
    "\n",
    "print(difference(22))\n",
    "print(difference(14))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##17. Write a Python program to test whether a number is within 100 of 1000 or 2000."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def near_thousand(n):\n",
    "      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))\n",
    "print(near_thousand(1000))\n",
    "print(near_thousand(900))\n",
    "print(near_thousand(800))   \n",
    "print(near_thousand(2200))\n",
    "print(near_thousand(1900))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "27\n"
     ]
    }
   ],
   "source": [
    "def three_numbers(a, b, c):\n",
    "    if (a == b) and (b ==c):\n",
    "        return (a+b+c)*3\n",
    "    else:\n",
    "        return (a+b+c)\n",
    "    \n",
    "print(three_numbers(1,2,3))\n",
    "print(three_numbers(3,3,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "27\n"
     ]
    }
   ],
   "source": [
    "def sum_thrice(x, y, z):\n",
    "\n",
    "     sum = x + y + z\n",
    "  \n",
    "     if x == y == z:\n",
    "      sum = sum * 3\n",
    "     return sum\n",
    "\n",
    "print(sum_thrice(1, 2, 3))\n",
    "print(sum_thrice(3, 3, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##19. Write a Python program to get a new string from a given string where \"Is\" has been added to the front. If the given string already begins with \"Is\" then return the string unchanged. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Isempty\n",
      "Isallow\n",
      "Ishello world Isempty\n"
     ]
    }
   ],
   "source": [
    "def string(str):\n",
    "    if len(str) >= 2 and str[:2]== 'Is':\n",
    "        return str\n",
    "    return \"Is\"+ str\n",
    "\n",
    "print(string('Isempty'))\n",
    "print(string('allow'))\n",
    "print(string('hello world Isempty'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##20. Write a Python program to get a string which is n (non-negative integer) copies of a given string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "orhanorhanorhanorhanorhan\n",
      ".py.py.py\n"
     ]
    }
   ],
   "source": [
    "def string(str):\n",
    "    return len(str)*(str)\n",
    "print(string('orhan'))\n",
    "print(string('.py'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcabc\n",
      ".py.py.py\n"
     ]
    }
   ],
   "source": [
    "def larger_string(str, n):\n",
    "   result = \"\"\n",
    "   for i in range(n):\n",
    "      result = result + str\n",
    "   return result\n",
    "\n",
    "print(larger_string('abc', 2))\n",
    "print(larger_string('.py', 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input a number : 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is even\n"
     ]
    }
   ],
   "source": [
    "x = int(input('Input a number :'))\n",
    "if x%2 == 1:\n",
    "    print('number is odd')\n",
    "else: \n",
    "    print('number is even')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is an even number.\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "mod = num % 2\n",
    "if mod > 0:\n",
    "    print(\"This is an odd number.\")\n",
    "else:\n",
    "    print(\"This is an even number.\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 22.Write a Python program to count the number 4 in a given list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "def number(n):\n",
    "    count = 0\n",
    "    for i in n: \n",
    "        if i == 4:\n",
    "            count = count + 1\n",
    "    return (count)\n",
    "\n",
    "print(number([2, 4 ,5 ,6 ,7 ,4 , 4 , 4, 4]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "def list_count_4(nums):\n",
    "  count = 0  \n",
    "  for num in nums:\n",
    "    if num == 4:\n",
    "      count = count + 1\n",
    "\n",
    "  return count\n",
    "\n",
    "print(list_count_4([1, 4, 6, 7, 4]))\n",
    "print(list_count_4([1, 4, 6, 4, 7, 4]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "yazdigim kod calismadi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-116-e29929920c13>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-116-e29929920c13>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    if x = len(str):\u001b[0m\n\u001b[1;37m         ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def string(str):\n",
    "    x = 2 \n",
    "    if x = len(str):\n",
    "    print((string)*n)\n",
    "    else: \n",
    "    print((string)[:1]*(n-1)+n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abab\n",
      "ppp\n"
     ]
    }
   ],
   "source": [
    "def substring_copy(str, n):\n",
    "  flen = 2\n",
    "  if flen > len(str):\n",
    "    flen = len(str)\n",
    "  substr = str[:flen]\n",
    "  \n",
    "  result = \"\"\n",
    "  for i in range(n):\n",
    "    result = result + substr\n",
    "  return result\n",
    "print(substring_copy('abcdef', 2))\n",
    "print(substring_copy('p', 3));"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##24. Write a Python program to test whether a passed letter is a vowel or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def vowel(i):\n",
    "    vowel = 'aeiou'\n",
    "    return i in vowel      \n",
    "print(vowel('c'))\n",
    "print(vowel('a'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##### fonksiyonu istedigimiz isimle tanitabiliriz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def orhan(ari):\n",
    "    orhan = 'aeiou'\n",
    "    return ari in orhan\n",
    "print(orhan('c'))\n",
    "print(orhan('e'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "25. Write a Python program to check whether a specified value is contained in a group of values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def list(i):\n",
    "    list = '[3, 1, 5, 8]'\n",
    "    return i in list\n",
    "print(list('3'))\n",
    "print(list('-1'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_group_member(group_data, n):\n",
    "    for value in group_data:\n",
    "        if n == value:\n",
    "            return True\n",
    "    return False\n",
    "print(is_group_member([1, 5, 8, 3], 3))\n",
    "print(is_group_member([5, 8, 3], -1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##26. Write a Python program to create a histogram from a given list of integers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "y = [2, 3, 6, 5]\n",
    "plt.hist(y, bins = 10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "**\n",
      "***\n",
      "******\n",
      "*****\n"
     ]
    }
   ],
   "source": [
    "def histogram( items ):\n",
    "    for n in items:\n",
    "        output = ''\n",
    "        times = n\n",
    "        while( times > 0 ):\n",
    "          output += '*'\n",
    "          times = times - 1\n",
    "        print(output)\n",
    "\n",
    "histogram([2, 3, 6, 5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "27. Write a Python program to concatenate all elements in a list into a string and return it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "151223\n"
     ]
    }
   ],
   "source": [
    "def list_data(list):\n",
    "    sonuc= ''\n",
    "    for i in list:\n",
    "        sonuc += str(i)\n",
    "    return sonuc\n",
    "\n",
    "print(list_data([1, 5, 12, 2, 3]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "386\n",
      "462\n",
      "418\n",
      "344\n",
      "236\n",
      "566\n",
      "978\n",
      "328\n",
      "162\n",
      "758\n",
      "918\n",
      "237\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def even_numbers(numbers):\n",
    "     for i in numbers:\n",
    "        if i == 237:\n",
    "            print(i)\n",
    "            break;\n",
    "        elif i%2 == 0:\n",
    "            print(i)\n",
    "print(even_numbers([    \n",
    "    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, \n",
    "    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, \n",
    "    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, \n",
    "    958,743, 527\n",
    "    ]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "386\n",
      "462\n",
      "418\n",
      "344\n",
      "236\n",
      "566\n",
      "978\n",
      "328\n",
      "162\n",
      "758\n",
      "918\n",
      "237\n"
     ]
    }
   ],
   "source": [
    "numbers = [    \n",
    "    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, \n",
    "    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, \n",
    "    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, \n",
    "    958,743, 527\n",
    "    ]\n",
    "\n",
    "for x in numbers:\n",
    "    if x == 237:\n",
    "        print(x)\n",
    "        break;\n",
    "    elif x % 2 == 0:\n",
    "        print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "color_list_1 = set([\"White\", \"Black\", \"Red\"])\n",
    "color_list_2 = set([\"Red\", \"Green\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Black', 'White'}"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "color_list_1 - color_list_2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'White', 'Black'}\n"
     ]
    }
   ],
   "source": [
    "color_list_1 = set([\"White\", \"Black\", \"Red\"])\n",
    "color_list_2 = set([\"Red\", \"Green\"])\n",
    "\n",
    "print(color_list_1.difference(color_list_2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##30. Write a Python program that will accept the base and height of a triangle and compute the area."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input base of triangle = 5\n",
      "Input height of triangle = 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Triangle area = 10.0\n"
     ]
    }
   ],
   "source": [
    "a = float(input('Input base of triangle ='))\n",
    "h = float(input('Input height of triangle ='))\n",
    "area = a*h/2\n",
    "print('Triangle area =', area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input the base :  5\n",
      "Input the height :  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "area =  10.0\n"
     ]
    }
   ],
   "source": [
    "b = int(input(\"Input the base : \"))\n",
    "h = int(input(\"Input the height : \"))\n",
    "\n",
    "area = b*h/2\n",
    "\n",
    "print(\"area = \", area)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\User\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py:2: DeprecationWarning: fractions.gcd() is deprecated. Use math.gcd() instead.\n",
      "  \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from fractions import gcd\n",
    "gcd(12,17)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "def gcd(x, y):\n",
    "    gcd = 1\n",
    "    \n",
    "    if x % y == 0:\n",
    "        return y\n",
    "    \n",
    "    for k in range(int(y / 2), 0, -1):\n",
    "        if x % k == 0 and y % k == 0:\n",
    "            gcd = k\n",
    "            break  \n",
    "    return gcd\n",
    "\n",
    "print(gcd(12, 17))\n",
    "print(gcd(4, 6))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 32. Write a Python program to get the least common multiple (LCM) of two positive integers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## cozemedim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "306\n"
     ]
    }
   ],
   "source": [
    "def lcm(x, y):\n",
    "   if x > y:\n",
    "       z = x\n",
    "   else:\n",
    "       z = y\n",
    "\n",
    "   while(True):\n",
    "       if((z % x == 0) and (z % y == 0)):\n",
    "           lcm = z\n",
    "           break\n",
    "       z += 1\n",
    "\n",
    "   return lcm\n",
    "print(lcm(4, 6))\n",
    "print(lcm(18, 17))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "0\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "def three_sum(x, y, z):\n",
    "    \n",
    "    a = int(x + y + z)\n",
    "    \n",
    "    if x == y or y == z or x == z:\n",
    "        print(0)\n",
    "    else:\n",
    "        print(a)\n",
    "        \n",
    "print(sum(2, 1, 2))\n",
    "print(sum(3, 2, 2))\n",
    "print(sum(2, 2, 2))\n",
    "print(sum(1, 2, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "0\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "def sum(x, y, z):\n",
    "    if x == y or y == z or x==z:\n",
    "        sum = 0\n",
    "    else:\n",
    "        sum = x + y + z\n",
    "    return sum\n",
    "\n",
    "print(sum(2, 1, 2))\n",
    "print(sum(3, 2, 2))\n",
    "print(sum(2, 2, 2))\n",
    "print(sum(1, 2, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "None\n",
      "12\n",
      "None\n",
      "22\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def sum_two(x, y):\n",
    "    sum = x + y\n",
    "    if sum > 15 and sum < 20:\n",
    "        print(20)\n",
    "    else: \n",
    "        print(sum)\n",
    "        \n",
    "print(sum_two(10, 6))\n",
    "print(sum_two(10, 2))\n",
    "print(sum_two(10, 12))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "12\n",
      "22\n"
     ]
    }
   ],
   "source": [
    "def sum(x, y):\n",
    "    sum = x + y\n",
    "    if sum in range(15, 20):\n",
    "        return 20\n",
    "    else:\n",
    "        return sum\n",
    "\n",
    "print(sum(10, 6))\n",
    "print(sum(10, 2))\n",
    "print(sum(10, 12))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "true\n",
      "true\n",
      "True\n",
      "false\n"
     ]
    }
   ],
   "source": [
    "def two(x,y):\n",
    "    if  x == y:\n",
    "        return True\n",
    "    elif x + y == 5:\n",
    "        return('true')\n",
    "    elif x - y == 5 or y - x == 5 :\n",
    "        return('true')\n",
    "    else:\n",
    "        return('false')\n",
    "    \n",
    "print(two(7, 2))\n",
    "print(two(3, 2))\n",
    "print(two(2, 2))\n",
    "print(two(2, 21))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def test_number5(x, y):\n",
    "    if x == y or abs(x-y) == 5 or (x+y) == 5:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "print(test_number5(7, 2))\n",
    "print(test_number5(3, 2))\n",
    "print(test_number5(2, 2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 36. Write a Python program to add two objects if both objects are an integer type."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "def add_numbers(a, b):\n",
    "    if not (isinstance(a, int) and isinstance(b, int)):\n",
    "         raise TypeError(\"Inputs must be integers\")\n",
    "    return a + b\n",
    "\n",
    "print(add_numbers(10, 20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##37. Write a Python program to display your details like name, age, address in three different lines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Orhan ARI\n",
      "Age: 35\n",
      "Adresses: Athens/Greece\n"
     ]
    }
   ],
   "source": [
    "print(\"\"\"Name: Orhan ARI\n",
    "Age: 35\n",
    "Adresses: Athens/Greece\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Simon\n",
      " Age: 19\n",
      " Address: Bangalore, Karnataka, India\n"
     ]
    }
   ],
   "source": [
    "def personal_details():\n",
    "    name, age = \"Simon\", 19\n",
    "    address = \"Bangalore, Karnataka, India\"\n",
    "    print(\"Name: {}\\n Age: {}\\n Address: {}\".format(name, age, address))\n",
    "\n",
    "personal_details()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 38. Write a Python program to solve (x + y) * (x + y)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "49\n"
     ]
    }
   ],
   "source": [
    "def kare(x,y):\n",
    "    top_kar = (x + y) * (x + y)\n",
    "    return(top_kar)\n",
    "    \n",
    "print(kare(4,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4 + 3) ^ 2) = 49\n"
     ]
    }
   ],
   "source": [
    "x, y = 4, 3\n",
    "result = x * x + 2 * x * y + y * y\n",
    "print(\"({} + {}) ^ 2) = {}\".format(x, y, result))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12722.79\n"
     ]
    }
   ],
   "source": [
    "amt = 10000\n",
    "int = 3.5\n",
    "years = 7\n",
    "\n",
    "result  = amt*((1+(0.01*int)) ** years)\n",
    "print(round(result,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.324555320336759\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "p1 = [4, 0]\n",
    "p2 = [6, 6]\n",
    "distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )\n",
    "\n",
    "print(distance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##41. Write a Python program to check whether a file exists."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os.path\n",
    "os.path.isfile('deneme.ipynb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'64bit'"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import platform\n",
    "platform.architecture()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## EDITORUN COZUMU"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "64\n"
     ]
    }
   ],
   "source": [
    "import struct\n",
    "print(struct.calcsize(\"P\") * 8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##43. Write a Python program to get OS name, platform and release information."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nt\n",
      "Windows\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "import platform\n",
    "import os\n",
    "print(os.name)\n",
    "print(platform.system())\n",
    "print(platform.release())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##44. Write a Python program to locate Python site-packages."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['C:\\\\Users\\\\User\\\\anaconda3', 'C:\\\\Users\\\\User\\\\anaconda3\\\\lib\\\\site-packages']\n"
     ]
    }
   ],
   "source": [
    "import site; \n",
    "print(site.getsitepackages())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.18.1\n",
      "blas_mkl_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/User/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/Users/User/anaconda3\\\\Library\\\\include']\n",
      "blas_opt_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/User/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/Users/User/anaconda3\\\\Library\\\\include']\n",
      "lapack_mkl_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/User/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/Users/User/anaconda3\\\\Library\\\\include']\n",
      "lapack_opt_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/User/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\include', 'C:\\\\Program Files (x86)\\\\IntelSWTools\\\\compilers_and_libraries_2019.0.117\\\\windows\\\\mkl\\\\lib', 'C:/Users/User/anaconda3\\\\Library\\\\include']\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "print(np.__version__)\n",
    "print(np.show_config())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "def toplama(x,y):\n",
    "    return(x+y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = toplama(3,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "40"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a*5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "toplama(4,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
