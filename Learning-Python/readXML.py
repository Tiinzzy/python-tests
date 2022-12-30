import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
import xml.etree.ElementTree as ET
import ssl

#URL: https://py4e-data.dr-chuck.net/comments_1703727.xml

data = ''' <commentinfo>
<note>This file contains the actual data for your assignment - good luck!</note>
<comments>
<comment>
<name>Lachlann</name>
<count>99</count>
</comment>
<comment>
<name>Chidi</name>
<count>99</count>
</comment>
<comment>
<name>Charli</name>
<count>97</count>
</comment>
<comment>
<name>Valery</name>
<count>95</count>
</comment>
<comment>
<name>Anesu</name>
<count>94</count>
</comment>
<comment>
<name>Clara</name>
<count>93</count>
</comment>
<comment>
<name>Ihtisham</name>
<count>92</count>
</comment>
<comment>
<name>Raymond</name>
<count>92</count>
</comment>
<comment>
<name>Zaya</name>
<count>87</count>
</comment>
<comment>
<name>Matthew</name>
<count>83</count>
</comment>
<comment>
<name>Connel</name>
<count>83</count>
</comment>
<comment>
<name>Autumn</name>
<count>80</count>
</comment>
<comment>
<name>Kyral</name>
<count>76</count>
</comment>
<comment>
<name>Fathima</name>
<count>75</count>
</comment>
<comment>
<name>Nevin</name>
<count>74</count>
</comment>
<comment>
<name>Amylee</name>
<count>70</count>
</comment>
<comment>
<name>Taliah</name>
<count>68</count>
</comment>
<comment>
<name>Mehek</name>
<count>67</count>
</comment>
<comment>
<name>Jarred</name>
<count>67</count>
</comment>
<comment>
<name>Amaarah</name>
<count>66</count>
</comment>
<comment>
<name>Isak</name>
<count>65</count>
</comment>
<comment>
<name>Nicol</name>
<count>63</count>
</comment>
<comment>
<name>Navdeep</name>
<count>62</count>
</comment>
<comment>
<name>Kristie</name>
<count>61</count>
</comment>
<comment>
<name>Dearbhla</name>
<count>61</count>
</comment>
<comment>
<name>Karina</name>
<count>53</count>
</comment>
<comment>
<name>Gabriella</name>
<count>51</count>
</comment>
<comment>
<name>Betsy</name>
<count>47</count>
</comment>
<comment>
<name>Sinead</name>
<count>45</count>
</comment>
<comment>
<name>Bradly</name>
<count>42</count>
</comment>
<comment>
<name>Meganlee</name>
<count>41</count>
</comment>
<comment>
<name>Karyn</name>
<count>39</count>
</comment>
<comment>
<name>Mhia</name>
<count>39</count>
</comment>
<comment>
<name>Areej</name>
<count>36</count>
</comment>
<comment>
<name>Suzi</name>
<count>29</count>
</comment>
<comment>
<name>Abbeygale</name>
<count>29</count>
</comment>
<comment>
<name>Joude</name>
<count>29</count>
</comment>
<comment>
<name>Aedin</name>
<count>27</count>
</comment>
<comment>
<name>Fia</name>
<count>26</count>
</comment>
<comment>
<name>Patsy</name>
<count>26</count>
</comment>
<comment>
<name>Hately</name>
<count>25</count>
</comment>
<comment>
<name>Rooke</name>
<count>21</count>
</comment>
<comment>
<name>Kaelan</name>
<count>20</count>
</comment>
<comment>
<name>Tracey</name>
<count>20</count>
</comment>
<comment>
<name>Cruiz</name>
<count>13</count>
</comment>
<comment>
<name>Tadd</name>
<count>13</count>
</comment>
<comment>
<name>Merin</name>
<count>5</count>
</comment>
<comment>
<name>Elice</name>
<count>5</count>
</comment>
<comment>
<name>Hallie</name>
<count>4</count>
</comment>
<comment>
<name>Rohit</name>
<count>2</count>
</comment>
</comments>
</commentinfo>'''

ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE 

tree = ET.fromstring(data)
numbers = tree.findall('comments/comment')

print('length count: ', len(numbers))

sum = 0
for num in numbers:
    allNum = num.find('count').text
    sum += int(allNum)
print('Total: ', sum)