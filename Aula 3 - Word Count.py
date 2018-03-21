#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:43:43 2018

@author: gustavoliu
"""
import string

text = """
If I speak in the tongues of men and of angels, but have not love,
 I am a noisy gong or a clanging cymbal. 2 And if I have prophetic powers,
 and understand all mysteries and all knowledge, and if I have all faith,
 so as to remove mountains, but have not love, I am nothing. 3 If I give away
 all I have, and if I deliver up my body to be burned,[a] but have not love,
 I gain nothing. 4 Love is patient and kind; love does not envy or boast;
 it is not arrogant 5 or rude. It does not insist on its own way;
 it is not irritable or resentful;[b] 6 it does not rejoice at wrongdoing,
 but rejoices with the truth. 7 Love bears all things, believes all things,
 hopes all things, endures all things. 8 Love never ends. As for prophecies,
 they will pass away; as for tongues, they will cease; as for knowledge,
 it will pass away. 9 For we know in part and we prophesy in part,
 10 but when the perfect comes, the partial will pass away.
 11 When I was a child, I spoke like a child, I thought like a child,
 I reasoned like a child. When I became a man, I gave up childish ways.
 12 For now we see in a mirror dimly, but then face to face.
 Now I know in part; then I shall know fully, even as I have been fully known.
 13 So now faith, hope, and love abide, these three;
 but the greatest of these is love.
"""


def freq_counter(txt):
    translator = str.maketrans('', '', string.punctuation)
    t = txt.lower().translate(translator)
    word_list = t.split()
    freq = [word_list.count(n) for n in word_list]
    print(text)
    print(sorted(set(zip(word_list, freq)), key=lambda x: x[1], reverse=True))


freq_counter(text)
