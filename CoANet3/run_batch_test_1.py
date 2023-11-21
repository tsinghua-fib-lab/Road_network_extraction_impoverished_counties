import os
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'江孜县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'红河县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'荔波县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'巫溪县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'融安县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'新田县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'靖宇县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'昆山市')

# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'洞口县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'上林县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'旺苍县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'越西县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'思南县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'从江县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'福贡县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'临夏县')

# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'大安市')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'汤原县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'明水县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'寿县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'宁都县')

# county_list = ['灵台县', '秭归县', '汝阳县', '印江土家族苗族自治县', '兰考县', '广宗县', '大新县', '保亭黎族苗族自治县', '蕲春县', '麻江县']
county_list = ['罗平县', '化隆回族自治县', '罗甸县']#'延长县', '繁峙县', '大姚县', '竹溪县', '兰西县', '彝良县','叙永县', '武定县', '崇礼区', '彭水苗族土家族自治县', '镇巴县', '永善县', '榕江县', '云县', '望谟县', '察哈尔右翼前旗']
for county in county_list:
    os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+county)