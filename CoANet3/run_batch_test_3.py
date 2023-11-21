import os
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'准格尔旗')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'闽侯县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'肥西县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'新郑市')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'沛县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'长兴县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'长丰县')
# os.system('python test4.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'高邮市')


# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'桂东县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'田阳县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'嵩县')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'巴林左旗')
# os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+'库伦旗')

# county_list = ['忻城县', '余干县', '沈丘县', '新蔡县', '朝天区', '岳西县', '普格县', '上犹县', '南部县', '循化撒拉族自治县']

county_list = ['绿春县', '通渭县', '务川仡佬族苗族自治县']#'永德县', '兴县', '新化县', '宁陕县', '神农架林区', '宁明县', '宁洱哈尼族彝族自治县', '遂川县', '耿马傣族佤族自治县', '陇西县', '习水县', '镇原县', '克东县', '临洮县', '凤庆县']
for county in county_list:
    os.system('python test3.py'+' '+'--ckpt=CoANet-DeepGlobe.pth.tar'+' '+'--out-path=./test_run'+' '+'--dataset=DeepGlobe'+' '+'--base-size=512'+' '+'--crop-size=512'+' '+'--district='+county)