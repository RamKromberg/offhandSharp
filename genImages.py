#!/usr/bin/env python3
from mingus.containers import Note
from copy import copy, deepcopy # abused all over
import drawsvg as draw

# a really ugly one-off script to generate layouts for the offhand# isomorphic layout
# https://github.com/RamKromberg/offhandSharp

root=Note("C-2")
sixByFour = True
invert=False
background = True
rightTrans = 2
downTrans = 4
offhandTrans = 7

if sixByFour:
	w, h = 6, 4
	imgH = 5.5
	imgW = 7.75
else:
	w, h = 7, 3
	imgH = 6.5
	imgW = 6

right = [[0 for x in range(w)] for y in range(h)]
left = [[0 for x in range(w)] for y in range(h)]
hands = [right, left]
handsLabels = ["Right", "Left"]

keysRight = [[0 for x in range(w)] for y in range(h)]
keysLeft = [[0 for x in range(w)] for y in range(h)]
keys = [keysRight, keysLeft]

# References:
# keys are c-c 3/4 of an inch so we'll stick to inches all over
# https://deskthority.net/wiki/KiCAD_keyboard_PCB_design_guide
# A4 = 1:1.414
# Letter (ANSI A) = 8.5/11
# https://bspaans.github.io/python-mingus/doc/wiki/tutorialNoteModule.html
# https://pypi.org/project/drawsvg/

class Hyperlink(draw.DrawingParentElement):
	TAG_NAME = 'a'
	def __init__(self, href, target=None, **kwargs):
		# Other init logic...
		# Keyword arguments to super().__init__() correspond to SVG node
		# arguments: stroke_width=5 -> <a stroke-width="5" ...>...</a>
		super().__init__(href=href, target=target, **kwargs)

note=copy(root)
for hand in hands:
	for row in range (h):
		for column in range(w):
			hand[row][column] = copy(note)
			note.transpose(str(rightTrans))
			note.from_int(int(note))
		note = copy(hand[row][0])
		note.transpose(str(downTrans))
		note.from_int(int(note))
	note = copy(hand[0][0])
	note.transpose(str(offhandTrans), up=False)
	note.octave_up()
	note.from_int(int(note))

print("debuging:")
print("right:")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in right]))
print("left:")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in left]))


spacing = 0.1
handsLabels = handsLabels[::-1] #reverse
d = draw.Drawing(str(imgW)+"in", str(imgH)+"in", origin=(0, 0))
if background:
	d.draw(draw.Rectangle(fill="white", x="0", y="0", width="100%", height="100%"))
for hand, _ in enumerate(hands):
	for row in range (h):
		for column in range(w):
			rectX = (imgW/18) + (0.75-(spacing/2))*row + (spacing/2)*row + (hand*imgW/2)
			rectY = (imgH/18) + (0.75-(spacing/2))*column + (spacing/2)*column
			rectWidth = 0.75-(spacing/2)
			rectHeight = rectWidth
			d.draw(draw.Rectangle(fill='none', stroke='black', x=str(rectX)+"in", y=str(rectY)+"in", width=str(rectWidth)+"in",height=str(rectHeight)+"in"))
			if invert:
				if (hand == 0):
					cell=hands[::-1][hand][::-1][row][::-1][column]
					keys[hand][row][column]=[rectX,rectY,rectWidth,rectHeight,copy(cell)]
				else:
					cell=hands[::-1][hand][row][::-1][column]
					keys[hand][row][column]=[rectX,rectY,rectWidth,rectHeight,copy(cell)]
			else:
				if (hand == 0):
					cell=hands[::-1][hand][row][::-1][column]
					keys[hand][row][column]=[rectX,rectY,rectWidth,rectHeight,copy(cell)]
				else:
					cell=hands[::-1][hand][::-1][row][::-1][column]
					keys[hand][row][column]=[rectX,rectY,rectWidth,rectHeight,copy(cell)]
			label=str(cell.name)+str(cell.octave)
			d.append(draw.Text(label, font_size=18, x=str(rectX+rectWidth/2)+"in", y=str(rectY+rectHeight/2)+"in", text_anchor="middle", dominant_baseline="central"))

	d.append(draw.Text(handsLabels[hand], font_size=18, x=str(rectX-(imgW/10))+"in", y=str(rectY+(imgH/6))+"in", text_anchor="middle", dominant_baseline="central"))

d.append(draw.Text("Mouthpiece", font_size=18, x=str(imgW/2)+"in", y=str(rectY+(imgH/5))+"in", text_anchor="middle", dominant_baseline="central"))
c = deepcopy(d)

if True: # just the empty layouts
	d = deepcopy(c)
	if invert:
		baseLabel=str(w)+"x"+str(h)+" inverted"
	else:
		baseLabel=str(w)+"x"+str(h)
	#d.append(draw.Text("offhand#"+baseLabel, font_size=18, x="0.25in", y=str(imgH-0.25)+"in", text_anchor="start"))
	hlink = Hyperlink('https://github.com/RamKromberg/offhandSharp', target='_blank')
	hlink.append(draw.Text("offhand#"+baseLabel, font_size=18, x="0.25in", y=str(imgH-0.25)+"in", text_anchor="start"))
	d.append(hlink)

	output="offhandSharp_"+baseLabel+".svg"
	output=output.replace("#", "SHARP")
	output=output.replace(" ", "_")
	d.save_svg("./images/"+output)

chromatic = ['C-2', 'C#-2', 'D-2', 'D#-2', 'E-2', 'F-2', 'F#-2', 'G-2', 'G#-2', 'A-2', 'A#-2', 'B-2']
majorScales = [] # mingus' scales module doesn't handle octaves and I'm too lazy to bother doing things properly
for pos, key in enumerate(chromatic):
	key = Note(key)
	key = Note().from_int(int(key))
	majorScales.append([str(key)])
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	majorScales[pos].append(str(key))
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	majorScales[pos].append(str(key))
	key.augment()
	key = Note().from_int(int(key))
	majorScales[pos].append(str(key))
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	majorScales[pos].append(str(key))
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	majorScales[pos].append(str(key))
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	majorScales[pos].append(str(key))
	#key.augment()
	#key = Note().from_int(int(key))
	#majorScales[pos].append(str(key))
minorScales = []
for pos, key in enumerate(chromatic):
	key = Note(key)
	key = Note().from_int(int(key))
	minorScales.append([str(key)])
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	minorScales[pos].append(str(key))
	key.augment()
	key = Note().from_int(int(key))
	minorScales[pos].append(str(key))
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	minorScales[pos].append(str(key))
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	minorScales[pos].append(str(key))
	key.augment()
	key = Note().from_int(int(key))
	minorScales[pos].append(str(key))
	key.augment()
	key.augment()
	key = Note().from_int(int(key))
	minorScales[pos].append(str(key))
	#key.augment()
	#key.augment()
	#key = Note().from_int(int(key))
	#minorScales[pos].append(str(key))

# major
for pos, key in enumerate(chromatic):
	d = deepcopy(c)
	nameSuffix=" "+key[:-2]
	if invert:
		baseLabel=str(w)+"x"+str(h)+" inverted"+nameSuffix
	else:
		baseLabel=str(w)+"x"+str(h)+nameSuffix
	#d.append(draw.Text("offhand#"+baseLabel, font_size=18, x="0.25in", y=str(imgH-0.25)+"in", text_anchor="start"))
	hlink = Hyperlink('https://github.com/RamKromberg/offhandSharp', target='_blank')
	hlink.append(draw.Text("offhand#"+baseLabel, font_size=18, x="0.25in", y=str(imgH-0.25)+"in", text_anchor="start"))
	d.append(hlink)

	# drawing scales
	for hand, _ in enumerate(hands):
		for row in range (h):
			for column in range(w):
				if (str(keys[hand][row][column][4]) in majorScales[pos]):
					centerX=keys[hand][row][column][0]+keys[hand][row][column][2]/2
					centerY=keys[hand][row][column][1]+keys[hand][row][column][3]/2
					d.append(draw.Circle(str(centerX)+"in", str(centerY)+"in", str(keys[hand][row][column][2]/3)+"in", fill='none', stroke_width=2, stroke='black'))


	output="offhandSharp_"+baseLabel+".svg"
	output=output.replace("#", "SHARP")
	output=output.replace(" ", "_")
	d.save_svg("./images/"+output)

# minor
for pos, key in enumerate(chromatic):
	d = deepcopy(c)
	nameSuffix=" "+key[:-2]+"m"
	if invert:
		baseLabel=str(w)+"x"+str(h)+" inverted"+nameSuffix
	else:
		baseLabel=str(w)+"x"+str(h)+nameSuffix
	#d.append(draw.Text("offhand#"+baseLabel, font_size=18, x="0.25in", y=str(imgH-0.25)+"in", text_anchor="start"))
	hlink = Hyperlink('https://github.com/RamKromberg/offhandSharp', target='_blank')
	hlink.append(draw.Text("offhand#"+baseLabel, font_size=18, x="0.25in", y=str(imgH-0.25)+"in", text_anchor="start"))
	d.append(hlink)

	# drawing scales
	for hand, _ in enumerate(hands):
		for row in range (h):
			for column in range(w):
				if (str(keys[hand][row][column][4]) in minorScales[pos]):
					centerX=keys[hand][row][column][0]+keys[hand][row][column][2]/2
					centerY=keys[hand][row][column][1]+keys[hand][row][column][3]/2
					d.append(draw.Circle(str(centerX)+"in", str(centerY)+"in", str(keys[hand][row][column][2]/3)+"in", fill='none', stroke_width=2, stroke='black'))


	output="offhandSharp_"+baseLabel+".svg"
	output=output.replace("#", "SHARP")
	output=output.replace(" ", "_")
	d.save_svg("./images/"+output)
