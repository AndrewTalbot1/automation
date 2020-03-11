'''
Some of the data has been changed for this repository
Turn off sleep mode sudo pmset -a standby 0
Turn on energy saver
This program finds all clincs to a nearby zipcode and saves the data to a csv
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time 
import pandas as pd
import html5lib
import json
from selenium.webdriver.common.alert import Alert
import re
import random
from random import randint
from time import sleep
from selenium.common.exceptions import NoAlertPresentException

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

# Run time approximately 2 hours

zip_list = ['01032\n', '01072\n', '01103\n', '01220\n', '01258\n', '01351\n', '01451\n', '01510\n', '01543\n', '01605\n', '01740\n',
    '01853\n', '01907\n', '01969\n', '02048\n', '02112\n', '02137\n', '02186\n', '02266\n', '02340\n', '02379\n', '02471\n',
    '02552\n', '02635\n', '02664\n', '02726\n', '02780\n', '02829\n', '02872\n', '02902\n', '03037\n', '03073\n', '03222\n', '03253\n',
    '03284\n', '03448\n', '03581\n', '03745\n', '03785\n', '03830\n', '03857\n', '03890\n', '04011\n', '04046\n', '04078\n', '04108\n',
    '04234\n', '04270\n', '04343\n', '04412\n', '04448\n', '04479\n', '04553\n', '04613\n', '04649\n', '04683\n', '04751\n', '04787\n',
    '04911\n', '04942\n', '04972\n', '05036\n', '05065\n', '05144\n', '05301\n', '05401\n', '05456\n', '05485\n', '05651\n', '05678\n',
    '05748\n', '05819\n', '05848\n', '05905\n', '06033\n', '06068\n', '06094\n', '06128\n', '06167\n', '06251\n', '06333\n', '06378\n',
    '06417\n', '06461\n', '06495\n', '06525\n', '06699\n', '06756\n', '06798\n', '06852\n', '06903\n', '07009\n', '07035\n', '07066\n',
    '07094\n', '07193\n', '07401\n', '07450\n', '07509\n', '07628\n', '07675\n', '07730\n', '07764\n', '07840\n', '07876\n', '07938\n',
    '08006\n', '08034\n', '08063\n', '08089\n', '08205\n', '08246\n', '08327\n', '08405\n', '08543\n', '08618\n', '08730\n', '08804\n',
    '08835\n', '08873\n', '10002\n', '10027\n', '10113\n', '10153\n', '10178\n', '10272\n', '10312\n', '10473\n', '10526\n',
    '10560\n', '10602\n', '10912\n', '10950\n', '10984\n', '11026\n', '11202\n', '11228\n', '11256\n', '11377\n', '11427\n', '11542\n',
    '11575\n', '11704\n', '11733\n', '11764\n', '11791\n', '11939\n', '11967\n', '12025\n', '12058\n', '12086\n', '12132\n', '12164\n',
    '12193\n', '12227\n', '12255\n', '12411\n', '12440\n', '12469\n', '12501\n', '12529\n', '12565\n', '12601\n', '12745\n', '12778\n',
    '12817\n', '12848\n', '12879\n', '12928\n', '12960\n', '12993\n', '13045\n', '13082\n', '13120\n', '13154\n', '13214\n', '13313\n',
    '13340\n', '13406\n', '13441\n', '13490\n', '13617\n', '13643\n', '13671\n', '13730\n', '13758\n', '13804\n', '13842\n', '14005\n',
    '14039\n', '14072\n', '14125\n', '14171\n', '14222\n', '14303\n', '14445\n', '14482\n', '14525\n', '14557\n', '14608\n',
    '14717\n', '14744\n', '14782\n', '14820\n', '14854\n', '14883\n', '15009\n', '15043\n', '15071\n', '15110\n', '15201\n', '15226\n',
    '15257\n', '15286\n', '15333\n', '15363\n', '15424\n', '15451\n', '15480\n', '15539\n', '15601\n', '15634\n', '15671\n', '15697\n',
    '15734\n', '15764\n', '15829\n', '15904\n', '15943\n', '16020\n', '16052\n', '16120\n', '16156\n', '16232\n', '16263\n', '16344\n',
    '16401\n', '16434\n', '16530\n', '16623\n', '16655\n', '16682\n', '16734\n', '16830\n', '16859\n', '16915\n', '16946\n', '17022\n',
    '17048\n', '17073\n', '17103\n', '17202\n', '17240\n', '17271\n', '17326\n', '17361\n', '17506\n', '17547\n', '17581\n', '17727\n',
    '17764\n', '17829\n', '17859\n', '17920\n', '17954\n', '18010\n', '18045\n', '18074\n', '18195\n', '18241\n', '18330\n', '18360\n',
    '18433\n', '18460\n', '18518\n', '18629\n', '18705\n', '18822\n', '18854\n', '18933\n', '18968\n', '19016\n', '19043\n', '19075\n',
    '19104\n', '19130\n', '19155\n', '19195\n', '19346\n', '19381\n', '19428\n', '19468\n', '19503\n', '19540\n', '19607\n', '19725\n',
    '19941\n', '19973\n', '20023\n', '20053\n', '20081\n', '20120\n', '20152\n', '20185\n', '20213\n', '20242\n', '20319\n',
    '20405\n', '20431\n', '20504\n', '20536\n', '20571\n', '20607\n', '20635\n', '20680\n', '20715\n', '20746\n', '20776\n', '20818\n',
    '20862\n', '20899\n', '21014\n', '21048\n', '21093\n', '21150\n', '21214\n', '21241\n', '21288\n', '21530\n', '21617\n', '21649\n',
    '21675\n', '21716\n', '21758\n', '21792\n', '21840\n', '21902\n', '22033\n', '22102\n', '22172\n', '22214\n', '22305\n', '22407\n',
    '22476\n', '22538\n', '22581\n', '22650\n', '22726\n', '22807\n', '22850\n', '22940\n', '22987\n', '23043\n', '23083\n', '23119\n',
    '23161\n', '23222\n', '23269\n', '23307\n', '23358\n', '23422\n', '23455\n', '23505\n', '23606\n', '23701\n', '23836\n', '23876\n',
    '23922\n', '23966\n', '24020\n', '24053\n', '24085\n', '24128\n', '24165\n', '24220\n', '24271\n', '24325\n', '24381\n', '24450\n',
    '24502\n', '24539\n', '24578\n', '24613\n', '24714\n', '24822\n', '24859\n', '24901\n', '24966\n', '25026\n', '25067\n', '25115\n',
    '25161\n', '25213\n', '25271\n', '25326\n', '25389\n', '25437\n', '25524\n', '25573\n', '25651\n', '25703\n', '25728\n', '25827\n',
    '25868\n', '25920\n', '25985\n', '26074\n', '26155\n', '26218\n', '26270\n', '26325\n', '26385\n', '26444\n', '26542\n', '26587\n',
    '26676\n', '26755\n', '26855\n', '27030\n', '27106\n', '27204\n', '27249\n', '27295\n', '27341\n', '27403\n', '27498\n', '27524\n',
    '27555\n', '27589\n', '27619\n', '27698\n', '27808\n', '27833\n', '27861\n', '27886\n', '27925\n', '27958\n', '28006\n', '28040\n',
    '28089\n', '28124\n', '28166\n', '28219\n', '28253\n', '28288\n', '28326\n', '28353\n', '28380\n', '28409\n', '28445\n', '28472\n',
    '28527\n', '28560\n', '28601\n', '28628\n', '28656\n', '28681\n', '28712\n', '28737\n', '28762\n', '28791\n', '29009\n', '29052\n',
    '29102\n', '29138\n', '29178\n', '29225\n', '29324\n', '29369\n', '29410\n', '29439\n', '29474\n', '29518\n', '29565\n', '29591\n',
    '29621\n', '29648\n', '29677\n', '29707\n', '29743\n', '29834\n', '29904\n', '29933\n', '30016\n', '30043'
    '30099\n', '30125\n', '30154\n', '30187\n', '30238\n', '30275\n', '30307\n', '30333\n', '30361\n', '30396\n', '30442\n', '30477\n', '30529\n',
    '30558\n', '30603\n', '30641\n', '30701\n', '30741\n', '30817\n', '30999\n', '31025\n', '31052\n', '31082\n', '31139\n', '31210\n',
    '31316\n', '31412\n', '31532\n', '31562\n', '31631\n', '31708\n', '31760\n', '31793\n', '31826\n', '32004\n', '32055\n', '32091\n',
    '32126\n', '32160\n', '32198\n', '32226\n', '32258\n', '32320\n', '32350\n', '32412\n', '32445\n', '32508\n', '32544\n',
    '32626\n', '32680\n', '32720\n', '32756\n', '32790\n', '32818\n', '32858\n', '32905\n', '32949\n', '33001\n', '33030\n', '33065\n',
    '33109\n', '33140\n', '33165\n', '33191\n', '33266\n', '33320\n', '33355\n', '33422\n', '33448\n', '33480\n', '33527\n', '33569\n',
    '33604\n', '33631\n', '33685\n', '33731\n', '33767\n', '33809\n', '33847\n', '33877\n', '33913\n', '33949\n', '33991\n', '34138\n',
    '34220\n', '34264\n', '34293\n', '34461\n', '34602\n', '34669\n', '34729\n', '34770\n', '34972\n', '35013\n', '35051\n', '35085\n',
    '35131\n', '35181\n', '35218\n', '35246\n', '35292\n', '35453\n', '35486\n', '35563\n', '35603\n', '35648\n', '35748\n', '35775\n',
    '35899\n', '35971\n', '36016\n', '36045\n', '36082\n', '36118\n', '36277\n', '36343\n', '36432\n', '36475\n', '36527\n',
    '36559\n', '36602\n', '36644\n', '36736\n', '36769\n', '36855\n', '36912\n', '37029\n', '37059\n', '37086\n', '37133\n', '37171\n',
    '37209\n', '37240\n', '37315\n', '37341\n', '37370\n', '37403\n', '37615\n', '37681\n', '37721\n', '37760\n', '37814\n', '37853\n',
    '37885\n', '37930\n', '38016\n', '38050\n', '38103\n', '38131\n', '38173\n', '38230\n', '38303\n', '38338\n', '38369\n', '38451\n',
    '38483\n', '38556\n', '38585\n', '38631\n', '38664\n', '38723\n', '38764\n', '38829\n', '38865\n', '38924\n', '38959\n', '39060\n',
    '39096\n', '39151\n', '39180\n', '39217\n', '39320\n', '39356\n', '39436\n', '39478\n', '39553\n', '39629\n', '39668\n', '39755\n',
    '39834\n', '40007\n', '40047\n', '40078\n', '40159\n', '40214\n', '40255\n', '40297\n', '40353\n', '40392\n', '40472\n', '40516\n',
    '40601\n', '40759\n', '40843\n', '40930\n', '40995\n', '41033\n', '41065\n', '41121\n', '41181\n', '41263\n', '41365\n', '41514\n',
    '41557\n', '41622\n', '41713\n', '41764\n', '41835\n', '42025\n', '42058\n', '42122\n', '42167\n', '42256\n', '42325\n', '42366\n',
    '42437\n', '42519\n', '42702\n', '42753\n', '43014\n', '43046\n', '43080\n', '43125\n', '43157\n', '43216\n', '43270\n', '43326\n',
    '43359\n', '43442\n', '43506\n', '43536\n', '43571\n', '43657\n', '43728\n', '43762\n', '43812\n', '43914\n', '43947\n', '44001\n',
    '44047\n', '44082\n', '44111\n', '44136\n', '44198\n', '44241\n', '44285\n', '44325\n', '44420\n', '44452\n', '44507\n', '44622\n',
    '44651\n', '44682\n', '44720\n', '44828\n', '44860\n', '44906\n', '45107\n', '45148\n', '45204\n', '45230\n', '45255\n',
    '45308\n', '45335\n', '45362\n', '45402\n', '45431\n', '45504\n', '45642\n', '45675\n', '45712\n', '45760\n', '45802\n', '45835\n',
    '45864\n', '45890\n', '46036\n', '46068\n', '46121\n', '46156\n', '46201\n', '46228\n', '46268\n', '46320\n', '46372\n', '46408\n',
    '46536\n', '46574\n', '46702\n', '46748\n', '46784\n', '46815\n', '46868\n', '46926\n', '46959\n', '46994\n', '47035\n', '47122\n',
    '47858\n', '47902\n', '47967\n', '47997\n', '48036\n', '48067\n', '48095\n', '48123\n', '48154\n', '48185\n',
    '48214\n', '48239\n', '48308\n', '48334\n', '48376\n', '48422\n', '48454\n', '48504\n', '48608\n', '48633\n', '48670\n', '48735\n',
    '48763\n', '48820\n', '48847\n', '48874\n', '48906\n', '49003\n', '49029\n', '49057\n', '49083\n', '49115\n', '49234\n', '49262\n',
    '49302\n', '49330\n', '49403\n', '49430\n', '49460\n', '49534\n', '49626\n', '49654\n', '49688\n', '49727\n', '49759\n', '49792\n',
    '49829\n', '49866\n', '49902\n', '49945\n', '50006\n', '50038\n', '50065\n', '50112\n', '50140\n', '50166\n', '50226\n', '50252\n',
    '50303\n', '50329\n', '50394\n', '50444\n', '50472\n', '50524\n', '50556\n', '50585\n', '50616\n', '50647\n', '50674\n', '50845\n',
    '51002\n', '51030\n', '51060\n', '51243\n', '51357\n', '51451\n', '51529\n', '51557\n', '51631\n', '52033\n', '52066\n', '52147\n',
    '52204\n', '52231\n', '52306\n', '52333\n', '52361\n', '52540\n', '52572\n', '52627\n', '52658\n', '52749\n', '52801\n', '53018\n',
    '53048\n', '53080\n', '53114\n', '53149\n', '53187\n', '53217\n', '53293\n', '53520\n', '53547\n', '53576\n', '53704\n', '53788\n',
    '53824\n', '53936\n', '53963\n', '54025\n', '54128\n', '54165\n', '54217\n', '54313\n', '54424\n', '54454\n', '54484\n', '54525\n',
    '54557\n', '54622\n', '54649\n', '54722\n', '54748\n', '54801\n', '54838\n', '54868\n', '54914\n', '54947\n', '54981\n', '55021\n',
    '55054\n', '55085\n', '55120\n', '55172\n', '55320\n', '55346\n', '55372\n', '55397\n', '55423\n', '55448\n', '55552\n', '55577\n',
    '55603\n', '55717\n', '55749\n', '55784\n', '55816\n', '55934\n', '55963\n', '56002\n', '56033\n', '56065\n', '56110\n', '56141\n',
    '56169\n', '56216\n', '56248\n', '56281\n', '56313\n', '56340\n', '56371\n', '56430\n', '56464\n', '56518\n', '56547\n', '56576\n',
    '56629\n', '56663\n', '56714\n', '56748'
    '57027\n', '57053\n', '57101\n', '57216\n', '57247\n', '57276\n', '57339\n',
    '57370\n', '57430\n', '57465\n', '57534\n', '57572\n', '57642\n', '57720\n', '57763\n', '58004\n', '58042\n', '58072\n', '58205\n',
    '58239\n', '58274\n', '58338\n', '58377\n', '58431\n', '58474\n', '58506\n', '58561\n', '58626\n', '58701\n', '58741\n', '58779\n',
    '58847\n', '59025\n', '59057\n', '59084\n', '59215\n', '59258\n', '59327\n', '59412\n', '59448\n', '59483\n', '59544\n', '59645\n',
    '59731\n', '59771\n', '59835\n', '59870\n', '59927\n', '60016\n', '60047\n', '60079\n', '60106\n', '60133\n', '60160\n', '60188\n',
    '60402\n', '60431\n', '60456\n', '60481\n', '60521\n', '60552\n', '60602\n', '60628\n', '60656\n', '60689\n', '60917\n', '60946\n',
    '61001\n', '61039\n', '61071\n', '61110\n', '61243\n', '61279\n', '61327\n', '61359\n', '61414\n', '61440\n', '61473\n', '61526\n',
    '61555\n', '61613\n', '61704\n', '61741\n', '61774\n', '61826\n', '61858\n', '61917\n', '62001\n', '62033\n', '62067\n', '62095\n',
    '62231\n', '62258\n', '62288\n', '62334\n', '62363\n', '62425\n', '62454\n', '62512\n', '62541\n', '62573\n', '62642\n', '62681\n',
    '62716\n', '62796\n', '62829\n', '62856\n', '62882\n', '62909\n', '62940\n', '62967\n', '62999\n', '63034\n', '63068\n', '63109\n',
    '63134\n', '63171\n', '63342\n', '63377\n', '63440\n', '63468\n', '63549\n', '63630\n', '63675\n', '63763\n', '63826\n', '63866\n',
    '63939\n', '64011\n', '64053\n', '64079\n', '64113\n', '64144\n', '64426\n', '64454\n', '64484\n', '64623\n', '64652\n',
    '64688\n', '64750\n', '64801\n', '64858\n', '65023\n', '65058\n', '65102\n', '65237\n', '65276\n', '65332\n', '65440\n', '65532\n',
    '65584\n', '65622\n', '65652\n', '65685\n', '65725\n', '65756\n', '65785\n', '66006\n', '66039\n', '66070\n', '66104\n', '66213\n',
    '66403\n', '66432\n', '66520\n', '66549\n', '66625\n', '66724\n', '66760\n', '66839\n', '66869\n', '66953\n', '67017\n', '67051\n',
    '67104\n', '67140\n', '67212\n', '67333\n', '67402\n', '67448\n', '67483\n', '67525\n', '67570\n', '67637\n', '67667\n', '67749\n',
    '67850\n', '67905\n', '68026\n', '68061\n', '68113\n', '68147\n', '68314\n', '68340\n', '68368\n', '68417\n', '68447\n', '68508\n',
    '68621\n', '68652\n', '68719\n', '68747\n', '68777\n', '68818\n', '68847\n', '68876\n', '68939\n', '68970\n', '69032\n', '69131\n',
    '69161\n', '69334\n', '69366\n', '70050\n', '70079\n', '70122\n', '70157\n', '70187\n', '70363\n', '70427\n', '70457\n', '70511\n',
    '70538\n', '70577\n', '70616\n', '70658\n', '70727\n', '70760\n', '70791\n', '70825\n', '71007\n', '71047\n', '71082\n', '71138\n',
    '71212\n', '71247\n', '71284\n', '71333\n', '71366\n', '71423\n', '71455\n', '71496\n', '71657\n', '71728\n', '71772\n', '71847\n',
    '71923\n', '71965\n', '72018\n', '72043\n', '72074\n', '72111\n', '72136\n', '72176\n', '72217\n', '72326\n', '72359\n', '72396\n',
    '72433\n', '72461\n', '72521\n', '72553\n', '72587\n', '72642\n', '72682\n', '72734\n', '72768\n', '72839\n', '72908\n', '72946\n',
    '73014\n', '73041\n', '73068\n', '73098\n', '73124\n', '73151\n', '73194\n', '73444\n', '73507\n', '73548\n', '73601\n', '73661\n',
    '73730\n', '73761\n', '73855\n', '74005\n', '74034\n', '74062\n', '74105\n', '74141\n', '74193\n', '74360\n', '74434\n', '74463\n',
    '74540\n', '74574\n', '74720\n', '74753\n', '74836\n', '74871\n', '74947\n', '75015\n', '75043\n', '75071\n', '75103\n', '75141\n',
    '75168\n', '75217\n', '75243\n', '75284\n', '75358\n', '75393\n', '75424\n', '75452\n', '75482\n', '75558\n', '75608\n', '75660\n',
    '75701\n', '75764\n', '75831\n', '75865\n', '75942\n', '75977\n', '76021\n', '76061\n', '76099\n', '76126\n', '76182\n', '76230\n',
    '76266\n', '76366\n', '76435\n', '76466\n', '76513\n', '76547\n', '76599\n', '76648\n', '76684\n', '76798\n', '76853\n', '76885\n',
    '76949\n', '77019\n', '77044\n', '77069\n', '77094\n', '77222'  
    '77468\n', '77496\n', '77531\n', '77565\n', '77612\n', '77656'
    '77802\n', '77857\n', '77904\n', '77984\n', '78016' 
    '78056\n', '78109\n', '78145\n', '78210\n', '78235\n', '78260\n', '78295'  
    '78358\n', '78389\n', '78460\n', '78521\n', '78561'
    '78589\n', '78617\n', '78644\n', '78672\n', '78717\n', '78744\n', '78769\n', '78837\n', '78886\n', '78960\n', '79029\n', '79063\n',
    '79096\n', '79172\n', '79244\n', '79330\n', '79370\n', '79414\n', '79517\n', '79547\n', '79702\n', '79742\n', '79778\n', '79849\n',
    '79923\n', '79950\n', '80007\n', '80036\n', '80118\n', '80162\n', '80223\n', '80251\n', '80302\n', '80426\n', '80455\n', '80488\n',
    '80532\n', '80612\n', '80653\n', '80746\n', '80819\n', '80866\n', '80925\n', '80951\n', '81025\n', '81063\n', '81126\n', '81155\n',
    '81241\n', '81334\n', '81433\n', '81621\n', '81653\n', '82063\n', '82229\n', '82421\n', '82524\n', '82712\n', '82840\n', '83001\n',
    '83201\n', '83234\n', '83277\n', '83332\n', '83405\n', '83446\n', '83531\n', '83607\n', '83641\n', '83680\n', '83726\n', '83815\n',
    '83848\n', '83877\n', '84027\n', '84054\n', '84080\n', '84107\n', '84132\n', '84201\n', '84325\n', '84412\n', '84536\n', '84635\n',
    '84665\n', '84733\n', '84759\n', '85002\n', '85027'
    '85086\n', '85143\n', '85215\n', '85267\n', '85295' 
    '85326\n', '85352\n', '85379\n', '85543\n', '85617\n', '85643\n', '85712\n', '85739\n', '85922\n', '86005\n', '86043\n', '86329\n', 
    '86413\n', '86506\n', '87010\n', '87038\n', '87101\n', '87144\n', '87310\n', '87413\n', '87515\n', '87545\n', '87579\n', '87734\n', 
    '87901\n', '88021\n', '88048\n', '88120\n', '88241\n', '88323\n', '88410\n', '88515\n', '88542\n', '88570\n', '89002\n', '89027\n', 
    '89061\n', '89116\n', '89141\n', '89166\n', '89404\n', '89431\n', '89504\n', '89705\n', '89883\n', '90025\n', '90050\n', '90075\n', 
    '90201\n', '90251\n', '90301\n', '90411\n', '90623\n', '90707\n', '90755\n', '90847\n', '91041\n', '91126\n', '91226\n', '91331\n', 
    '91402\n', '91504\n', '91617\n', '91741\n', '91771\n', '91896\n', '91943\n', '92014\n', '92055\n', '92086\n', '92119\n', 
    '92149\n', '92177\n', '92225\n', '92256\n', '92286\n', '92328\n', '92363\n', '92398\n', '92506\n', '92552\n', '92593\n', '92628\n', 
    '92675\n', '92821\n', '92862\n', '93005\n', '93042\n', '93117\n', '93221\n', '93252\n', '93283\n', '93385\n', '93430\n', 
    '93457\n', '93526\n', '93558\n', '93613\n', '93641\n', '93670\n', '93725\n', '93778\n', '93925\n', '94017\n', '94063\n', '94114\n', 
    '94139\n', '94248\n', '94285\n', '94497\n', '94526\n', '94552\n', '94578\n', '94607\n', '94702\n', '94913\n', '94949\n', 
    '94999\n', '95031\n', '95064\n', '95121\n', '95154\n', '95208\n', '95237\n', '95306\n', '95334\n', '95364\n', '95397\n', '95429\n', 
    '95459\n', '95493\n', '95545\n', '95585\n', '95623\n', '95651\n', '95677\n', '95709\n', '95798\n', '95834\n', '95914\n', '95942\n', 
    '95969\n', '96006\n', '96035\n', '96067\n', '96097\n', '96125\n', '96157\n', '96725\n', '96752\n', '96779\n', '96809\n', '96839\n', 
    '97009\n', '97036\n', '97068\n', '97117\n', '97146\n', '97222\n', '97266\n', '97307\n', '97343\n', '97374\n', '97408\n', '97437\n', 
    '97464\n', '97493\n', '97536\n', '97636\n', '97737\n', '97825\n', '97862\n', '97908\n', '98020\n', '98046\n', '98082\n', '98121\n', 
    '98164\n', '98206\n', '98243\n', '98273\n', '98305\n', '98340\n', '98367\n', '98395\n', '98431\n', '98497\n', '98533\n', '98564\n', 
    '98593\n', '98624\n', '98663\n', '98815\n', '98847\n', '98925\n', '99003\n', '99033\n', '99124\n', '99153\n', '99202\n', '99258\n', 
    '99348\n', '99509\n', '99556\n', '99603\n', '99644\n', '99678\n', '99714\n', '99748\n', '99782\n' ]

#zip_list =[] # Use to test zipcode
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://app.health-street.net/order/drug")
python_button = driver.find_element_by_class_name('item-left-justified')
python_button.click()
driver.implicitly_wait(10)
python_button_2 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "web-cat-group", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "item-right-justified", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "add-test-button", " " ))]')
python_button_2.click()

# Loops through all zip codes in the list above
for zip_code in zip_list:
    #Add a try block because sometimes the url reroutes itself, and I don't know why.
    try:
        elem = driver.find_element_by_id("zipInput")
        elem.clear()
        # Creates a wait function so the program doesn't get banned
        time.sleep(random.randint(1, 3)) 
        elem.send_keys(zip_code)
        driver.implicitly_wait(10)
        search_button = driver.find_element_by_class_name('magnifying-glass-button')
        search_button.click()
        driver.implicitly_wait(10)
        # Waits until the page has loaded
        time.sleep(5) 
    except:
        driver.get("https://app.health-street.net/order/drug")
        python_button = driver.find_element_by_class_name('item-left-justified')
        python_button.click()
        driver.implicitly_wait(10)
        python_button_2 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "web-cat-group", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "item-right-justified", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "add-test-button", " " ))]')
        python_button_2.click()

#####################################
#html_doc = driver.page_source
#soup = BeautifulSoup(html_doc, 'html.parser')
##### Use to find html structures####
#pretty_soup = (soup.prettify())
#with open("health_clients.html", "w") as file:
    #file.write(pretty_soup)
#####################################

    # Handles any pop up errors from a bad zipcode
    try:
        time.sleep(1)
        Alert(driver).accept()
    # Prints to terminal for later removal
        print(zip_code)
    
    except NoAlertPresentException:
        # Creates an HTML parser 
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        soup_2 = soup.find_all('div', class_="list-item vendor-list-item")

    # Sometimes the try Alert clause wont find the popup

        # Create an empty list to append to
        names = []
        roads = []
        suites = []
        city_state_zips = []
        registrations = []
        bar_codes = []
        monday = []
        monday_lunch = []
        tuesday = []
        tuesday_lunch = []
        wednesday = []
        wednesday_lunch = []
        thursday = []
        thursday_lunch = []
        friday = []
        friday_lunch = []
        saturday = []
        saturday_lunch = []
        sunday = []
        sunday_lunch = []

        # Loop though each span to find text
        
        for row in soup_2:
            cells = row.find_all("span")
            
            try:
                pass
                name = cells[0].get_text()
                names.append(name)
            except IndexError:
                names.append([])

            try:
                pass
                road = cells[1].get_text()
                roads.append(road)
            except IndexError:
                roads.append([])

            #Use if else statements because each result is different
            try:
                pass
                suite = re.search(('Suite|Unit|Building|Fl'), cells[2].get_text())
                if suite:
                    suites.append(cells[2].get_text())
                    city_state_zip = cells[3].get_text() 
                    city_state_zips.append(city_state_zip)
                else:
                    suite = []
                    suites.append(suite)
                    city_state_zip = cells[2].get_text() 
                    city_state_zips.append(city_state_zip)
            except IndexError:
                suites.append([])
                city_state_zips.append([])

            try:
                pass
                registration = re.search(('registration'), cells[4].get_text())
                if registration:
                    registrations.append(cells[4].get_text())
                    bar_code = cells[5].get_text()
                    bar_codes.append(bar_code)
                else:
                    registrations.append(cells[3].get_text())
                    bar_code = cells[4].get_text()
                    bar_codes.append(bar_code)
            except IndexError:
                #monday.append(cells[4].get_text())
                registrations.append([])
                bar_codes.append([])

            #MONDAY
            try:
                pass
                m = re.search(('M:'), cells[5].get_text())
                if m:
                    monday.append(cells[5].get_text())
                else:
                    monday.append(cells[6].get_text())
            except IndexError:
                try:
                    pass
                    m = re.search(('M-'), cells[3].get_text())
                    if m:
                        monday.append(cells[3].get_text())
                    else:
                        monday.append(['Call For Hours'])
                except IndexError:
                    monday.append([])
            
            #MONDAY LUNCH
            try:
                pass
                ml = re.search(('M Lunch:'), cells[6].get_text())
                ml_2 = re.search(('M Lunch:'), cells[7].get_text())
                if ml:
                    monday_lunch.append(cells[6].get_text())
                elif ml_2:
                    monday_lunch.append(cells[7].get_text())
                else: 
                    monday_lunch.append([])

            except IndexError:
                monday_lunch.append([])
    
            #TUESDAY

            try:
                pass
                t = re.search(('T:'), cells[6].get_text())
                t_2 = re.search(('T:'), cells[7].get_text())
                t_3 = re.search(('T:'), cells[8].get_text())
                if t:
                    tuesday.append(cells[6].get_text())
                elif t_2:
                    tuesday.append(cells[7].get_text())
                else:
                    tuesday.append(cells[8].get_text())

            except IndexError:
                tuesday.append([])
            #TUESDAY LUNCH
            
            try:
                pass
                tl = re.search(('T Lunch:'), cells[7].get_text())
                tl_2 = re.search(('T Lunch:'), cells[8].get_text())
                tl_3 = re.search(('T Lunch:'), cells[9].get_text())
                if tl:
                    tuesday_lunch.append(cells[7].get_text())
                elif tl_2:
                    tuesday_lunch.append(cells[8].get_text())
                elif tl_3:
                    tuesday_lunch.append(cells[9].get_text())
                else:
                    tuesday_lunch.append([])

            except IndexError:
                tuesday_lunch.append([])

            #WEDNESDAY

            try: 
                pass
                w = re.search(('W:'), cells[7].get_text())
                w_2 = re.search(('W:'), cells[8].get_text())
                w_3 = re.search(('W:'), cells[9].get_text())
                if w:
                    wednesday.append(cells[7].get_text())
                elif w_2:
                    wednesday.append(cells[8].get_text())
                elif w_3:
                    wednesday.append(cells[9].get_text())
                else:
                    wednesday.append(cells[10].get_text())
            
            except IndexError:
                wednesday.append([])

            #WEDNESDAY LUNCH

            try:
                pass
                wl = re.search(('W Lunch:'), cells[10].get_text())
                wl_2 = re.search(('W Lunch:'), cells[11].get_text())
                if w:
                    wednesday_lunch.append([])
                elif w_2:
                    wednesday_lunch.append([])
                elif ml:
                    wednesday_lunch.append(cells[10].get_text())
                elif wl:
                    wednesday_lunch.append(cells[10].get_text())
                elif suite:
                    wednesday_lunch.append(cells[11].get_text())
                else:
                    wednesday_lunch.append([])
            except IndexError:
                wednesday_lunch.append([])
            

            #THURSDAY checkes against the wednesday if block and monday lunch if block

            try:
                pass
            
                if w:
                    thursday.append(cells[8].get_text())
                elif w_2:
                    thursday.append(cells[9].get_text())
                #elif w_3:
                #    thursday.append(cells[10].get_text())
                elif wl: 
                    thursday.append(cells[11].get_text())
                else:
                    thursday.append(cells[12].get_text())

            except IndexError:
                thursday.append([])
            #THURSDAY LUNCH checkes against the wednesday if block and monday lunch if block
            try:
                pass
                if w:
                    thursday_lunch.append([])
                elif w_2:
                    thursday_lunch.append([])
                #elif w_3:
                    #thursday_lunch.append(cells[11].get_text())
                elif ml:
                    thursday_lunch.append(cells[12].get_text())
                else:
                    thursday_lunch.append(cells[13].get_text())
            except IndexError:
                thursday_lunch.append([])



            #FRIDAY checkes against the wednesday if block and monday lunch if block
            try:
                pass
                if w:
                    friday.append(cells[9].get_text())
                elif w_2:
                    friday.append(cells[10].get_text())
                #elif w_3:
                    #friday.append(cells[12].get_text())
                elif ml: 
                    friday.append(cells[13].get_text())
                else:
                    friday.append(cells[14].get_text())

            except IndexError:
                friday.append([])

            # FRIDAY LUNCH checkes against the wednesday if block and monday lunch if block
            try:
                pass
                if w:
                    friday_lunch.append([])
                elif w_2:
                    friday_lunch.append([])
                #elif w_3:
                #    friday_lunch.append(cells[13].get_text())
                elif ml:
                    friday_lunch.append(cells[14].get_text())
                else:
                    friday_lunch.append(cells[15].get_text())

            except IndexError:
                friday_lunch.append([])
            
            # SATURDAY
            try:
                sa = re.search(('Sa:'), cells[10].get_text())
                sa_2 = re.search(('Sa:'), cells[11].get_text())
                if sa:
                    saturday.append(cells[10].get_text())
                elif sa_2:
                    saturday.append(cells[11].get_text())
                elif ml: 
                    saturday.append(cells[15].get_text())
                else:
                    saturday.append(cells[16].get_text())

            except:
                sa = []
                sa_2 = []
                saturday.append([])

            # SATURDAY_LUNCH
            try:
                pass
                sl = re.search(('Sa Lunch:'), cells[11].get_text())
                sl_2 = re.search(('Sa Lunch:'), cells[16].get_text())
                sl_3 = re.search(('Sa Lunch:'), cells[17].get_text())
                if sl:
                    saturday_lunch.append(cells[11].get_text())
                elif sl_2:
                    saturday_lunch.append(cells[16].get_text())
                elif sl_3:
                    saturday_lunch.append(cells[17].get_text())
                else:
                    saturday_lunch.append([])
            except IndexError:
                saturday_lunch.append([])

            # SUNDAY Checks against the Saturday loop
            try:
                sund = re.search(('Su:'), cells[17].get_text())
                sund_2 = re.search(('Su:'), cells[18].get_text())
                if sa:
                    sunday.append(cells[11].get_text())
                elif sa_2:
                    sunday.append(cells[12].get_text())
                elif ml: 
                    sunday.append(cells[16].get_text())
                elif sund:
                    sunday.append(cells[17].get_text())
                else:
                    sunday.append(cells[18].get_text())
            except:
                sunday.append([])

            #SUNDAY LUNCH
            try:
                pass
                sundaylunch = re.search(('Su Lunch:'), cells[18].get_text())
                sundaylunch2 = re.search(('Su Lunch:'), cells[19].get_text())
                if sundaylunch:
                    sunday_lunch.append(cells[18].get_text())
                elif sundaylunch2:
                    sunday_lunch.append(cells[19].get_text())
                else:
                    sunday_lunch.append([])
            except:
                sunday_lunch.append([])
           
        # Saves the empty lists we started out with, with the appended values from the loop
        df = pd.DataFrame({
            'name': names,
            'road': roads,
            'suite': suites,
            'city_state_zip': city_state_zips,
            'registration': registrations,
            'bar_code': bar_codes,
            'monday': monday,
            'monday_lunch': monday_lunch,
            'tuesday': tuesday,
            'tuesday_lunch': tuesday_lunch,
            'wednesday': wednesday,
            'wednesday_lunch': wednesday_lunch,
            'thursday': thursday,
            'thursday_lunch': thursday_lunch,
            'friday': friday,
            'friday_lunch': friday_lunch,
            'saturday': saturday,
            'saturday_lunch': saturday_lunch, 
            'sunday': sunday,
            'sunday_lunch': sunday_lunch
            })
        
        columns = df[[
            'name', 
            'road',
            'suite', 
            'city_state_zip', 
            'registration',
            'bar_code', 
            'monday', 
            'monday_lunch', 
            'tuesday', 
            'tuesday_lunch', 
            'wednesday', 
            'wednesday_lunch', 
            'thursday',
            'thursday_lunch', 
            'friday', 
            'friday_lunch', 
            'saturday',
            'saturday_lunch',
            'sunday',
            'sunday_lunch'
            ]]

        df.columns = [ 'name', 'road' ,'suite', 'city_state_zip', 'registration','bar_code',
        'monday', 'monday_lunch', 'tuesday', 'tuesday_lunch', 'wednesday', 'wednesday_lunch',
        'thursday', 'thursday_lunch', 'friday', 'friday_lunch', 'saturday', 'saturday_lunch', 'sunday', 'sunday_lunch']


        df.to_csv('Userpath', mode = 'a', index=False)

driver.close()

# cleans all data that was scraped to unique
inFile = open('5_Panel_Drug_Test.csv','r')

outFile = open('5_Panel_Drug_Test_cleaned.csv','w')

listLines = []

for line in inFile:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()