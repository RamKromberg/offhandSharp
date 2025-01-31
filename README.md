# offhand#
[isomorphic](https://en.wikipedia.org/wiki/Isomorphic_keyboard) layout for [EWI](https://en.wikipedia.org/wiki/Electronic_wind_instrument)s

## Summary:

offhand# is a fingering layout for an electronic wind instrument that pursues:
1. Consistent fingerings across keys (a.k.a. isomorphism): All major keys are fingered the same. All minor keys are fingered the same. Chords and patterns follow, retaining the same fingering across all keys.
2. Chromatic approach: Accidentals are always within immediate reach and are easy to key.
3. Minimal position shifts: Diatonics are always within immediate reach and are easy to key.
4. All major and minor keys are playable: The minimal range is c2-a#3 (= 23 consecutive tones at least) without octave shifting.
5. No glitching: Apart from octave shifters, sustain and mod wheel for bending, no accidental modifiers (keys dedicated to sharp and flat) are used and the un-fingered (no keys pressed) position doesn't produce sound. The expanded range also means there's less breaks to work around.
6. Ergonomic with minimal position shifting: The use of a 6x4 / 7x3 split keyboard with 3/4in keys is widespread with plenty speed and accuracy oriented ergonomic designs (staggering the columns... concave... tenting...) around to choose from.
7. Polyphony and chording: Though not a design goal, Jazz guitar-style chord-melody voice leading versatility is achieved with a sustain key / pedal.

## Breakdown:

As its name suggests, the offhand# layout projects to the left hand by a semi-tone's worth (minor second); With a whole tone's worth (major second) on the X axis and five semitones (perfect fourth) on the Y axis:

![offhand#6x4](./images/offhandSharp_6x4.svg)

The result is that all major scales are played single-handedly across two rows without wrist position changes:

![offhand#6x4 C Major](./images/offhandSharp_6x4_C.svg)

![offhand#6x4 C# Major](./images/offhandSharp_6x4_CSHARP.svg)

![offhand#6x4 A Major](./images/offhandSharp_6x4_A.svg)

![offhand#6x4 A#](./images/offhandSharp_6x4_ASHARP.svg)

That is: 1st row right index -> 1st row right middle -> 1st row right ring -> 1st row right pinky -> 2nd row right index -> 2nd row right middle -> 2nd row right ring.

The minor keys are played using both hands but they too are limited to two rows and don't require position changes:

![offhand#6x4 A Minor](./images/offhandSharp_6x4_Am.svg)

![offhand#6x4 A# Minor](./images/offhandSharp_6x4_ASHARPm.svg)

That is: 1st row right index -> 1st row right middle -> 2nd row left index -> 2nd row right index -> 2nd row right middle finger -> 1st row left index finger -> 1st row left middle finger.

Chromatic runs follow with no wrist position changes.

## Instrument design and the thumb

Comparable to accordions, guitars and the [Berglund Instruments' NuRAD](https://berglundinstruments.com/nurad-ewi-sax-etc-fingering-instrument/), the offhand# is designed for an instrument that is supported by a strap with prongs at both sides with the arms being held without pronation or supination at parallel and the hands and thumbs being left free from having to stabilize and support. Thus, the right thumb is employed to shift octaves through the use of touch surfaces or an octave roller while the left thumb is used to trigger a sustain key or a pitch bending mod wheel / joystick / touch surface.

Breath control through a differential pressure sensor is, of course, a given for an electronic wind instrument. Refer to the [Haxophone](https://github.com/cardonabits/haxo-hw) for details.

A gyro-accelerometer chip may be employed as an additional control channel to trigger the likes of a saxophone growl, vibrato or a cello's bow work.

Bite sensors could also be incorporated into the design as a control channel.

### Alternative keyboard-like design

It's also possible to step away from the EWI design into a keyboard design by modifying existing mechanical keyboards where the thumbs rest at the sides and outfitting them with 4 thumb keys on the right for octave shifting and a button and thumb joystick on the left for sustain and bending.

## Inverted variation

The surveying of different ergonomic keyboard models suggests some players might prefer not utilizing their pinky in the last column at the bottom row while others may prefer avoiding the last column's top row. For them, an inverted layout is presented:

![offhand#6x4 inverted](./images/offhandSharp_6x4_inverted.svg)

## 7x3 variation and its inversion

It's also common to see keyboard users removing the numbers row altogether. Though this will necessitate a bit of wrist movement (like an accordion or guitar but considerably less than either), a 7x3 layout could be made available:

![offhand#7x3](./images/offhandSharp_7x3.svg)

An inverted variant is also presented if only to accommodate inverted 6x4 players wishing to experiment with 7x3 layouts:

![offhand#7x3 inverted](./images/offhandSharp_7x3_inverted.svg)

## MOAR!

<details>
  <summary>The rest of the 6x4 major scales</summary>

![offhand#6x4 B](./images/offhandSharp_6x4_B.svg)

![offhand#6x4 D](./images/offhandSharp_6x4_D.svg)

![offhand#6x4 D#](./images/offhandSharp_6x4_DSHARP.svg)

![offhand#6x4 E](./images/offhandSharp_6x4_E.svg)

![offhand#6x4 F](./images/offhandSharp_6x4_F.svg)

![offhand#6x4 F#](./images/offhandSharp_6x4_FSHARP.svg)

![offhand#6x4 G](./images/offhandSharp_6x4_G.svg)

![offhand#6x4 G#](./images/offhandSharp_6x4_GSHARP.svg)

</details>

<details>
  <summary>The rest of the 6x4 minor scales</summary>

![offhand#6x4 Bm](./images/offhandSharp_6x4_Bm.svg)

![offhand#6x4 Cm](./images/offhandSharp_6x4_Cm.svg)

![offhand#6x4 C#m](./images/offhandSharp_6x4_CSHARPm.svg)

![offhand#6x4 Dm](./images/offhandSharp_6x4_Dm.svg)

![offhand#6x4 D#m](./images/offhandSharp_6x4_DSHARPm.svg)

![offhand#6x4 Em](./images/offhandSharp_6x4_Em.svg)

![offhand#6x4 Fm](./images/offhandSharp_6x4_Fm.svg)

![offhand#6x4 F#m](./images/offhandSharp_6x4_FSHARPm.svg)

![offhand#6x4 Gm](./images/offhandSharp_6x4_Gm.svg)

![offhand#6x4 G#m](./images/offhandSharp_6x4_GSHARPm.svg)

</details>

<details>
  <summary>The inverted 6x4 major scales</summary>

![offhand#6x4 inverted A](./images/offhandSharp_6x4_inverted_A.svg)

![offhand#6x4 inverted A#](./images/offhandSharp_6x4_inverted_ASHARP.svg)

![offhand#6x4 inverted B](./images/offhandSharp_6x4_inverted_B.svg)

![offhand#6x4 inverted C](./images/offhandSharp_6x4_inverted_C.svg)

![offhand#6x4 inverted C#](./images/offhandSharp_6x4_inverted_CSHARP.svg)

![offhand#6x4 inverted D](./images/offhandSharp_6x4_inverted_D.svg)

![offhand#6x4 inverted D#](./images/offhandSharp_6x4_inverted_DSHARP.svg)

![offhand#6x4 inverted E](./images/offhandSharp_6x4_inverted_E.svg)

![offhand#6x4 inverted F](./images/offhandSharp_6x4_inverted_F.svg)

![offhand#6x4 inverted F#](./images/offhandSharp_6x4_inverted_FSHARP.svg)

![offhand#6x4 inverted G](./images/offhandSharp_6x4_inverted_G.svg)

![offhand#6x4 inverted G#](./images/offhandSharp_6x4_inverted_GSHARP.svg)

</details>

<details>
  <summary>The inverted 6x4 minor scales</summary>

![offhand#6x4 inverted Am](./images/offhandSharp_6x4_inverted_Am.svg)

![offhand#6x4 inverted A#m](./images/offhandSharp_6x4_inverted_ASHARPm.svg)

![offhand#6x4 inverted Bm](./images/offhandSharp_6x4_inverted_Bm.svg)

![offhand#6x4 inverted Cm](./images/offhandSharp_6x4_inverted_Cm.svg)

![offhand#6x4 inverted C#m](./images/offhandSharp_6x4_inverted_CSHARPm.svg)

![offhand#6x4 inverted Dm](./images/offhandSharp_6x4_inverted_Dm.svg)

![offhand#6x4 inverted D#m](./images/offhandSharp_6x4_inverted_DSHARPm.svg)

![offhand#6x4 inverted Em](./images/offhandSharp_6x4_inverted_Em.svg)

![offhand#6x4 inverted Fm](./images/offhandSharp_6x4_inverted_Fm.svg)

![offhand#6x4 inverted F#m](./images/offhandSharp_6x4_inverted_FSHARPm.svg)

![offhand#6x4 inverted Gm](./images/offhandSharp_6x4_inverted_Gm.svg)

![offhand#6x4 inverted G#m](./images/offhandSharp_6x4_inverted_GSHARPm.svg)

</details>

<details>
  <summary>The 7x3 major scales</summary>

![offhand#7x3 A](./images/offhandSharp_7x3_A.svg)

![offhand#7x3 A#](./images/offhandSharp_7x3_ASHARP.svg)

![offhand#7x3 B](./images/offhandSharp_7x3_B.svg)

![offhand#7x3 C](./images/offhandSharp_7x3_C.svg)

![offhand#7x3 C#](./images/offhandSharp_7x3_CSHARP.svg)

![offhand#7x3 D](./images/offhandSharp_7x3_D.svg)

![offhand#7x3 D#](./images/offhandSharp_7x3_DSHARP.svg)

![offhand#7x3 E](./images/offhandSharp_7x3_E.svg)

![offhand#7x3 F](./images/offhandSharp_7x3_F.svg)

![offhand#7x3 F#](./images/offhandSharp_7x3_FSHARP.svg)

![offhand#7x3 G](./images/offhandSharp_7x3_G.svg)

![offhand#7x3 G#](./images/offhandSharp_7x3_GSHARP.svg)

</details>

<details>
  <summary>The 7x3 minor scales</summary>

![offhand#7x3 Am](./images/offhandSharp_7x3_Am.svg)

![offhand#7x3 A#m](./images/offhandSharp_7x3_ASHARPm.svg)

![offhand#7x3 Bm](./images/offhandSharp_7x3_Bm.svg)

![offhand#7x3 Cm](./images/offhandSharp_7x3_Cm.svg)

![offhand#7x3 C#m](./images/offhandSharp_7x3_CSHARPm.svg)

![offhand#7x3 Dm](./images/offhandSharp_7x3_Dm.svg)

![offhand#7x3 D#m](./images/offhandSharp_7x3_DSHARPm.svg)

![offhand#7x3 Em](./images/offhandSharp_7x3_Em.svg)

![offhand#7x3 Fm](./images/offhandSharp_7x3_Fm.svg)

![offhand#7x3 F#m](./images/offhandSharp_7x3_FSHARPm.svg)

![offhand#7x3 Gm](./images/offhandSharp_7x3_Gm.svg)

![offhand#7x3 G#m](./images/offhandSharp_7x3_GSHARPm.svg)

</details>

<details>
  <summary>The inverted 7x3 major scales</summary>

![offhand#7x3 inverted A](./images/offhandSharp_7x3_inverted_A.svg)

![offhand#7x3 inverted A#](./images/offhandSharp_7x3_inverted_ASHARP.svg)

![offhand#7x3 inverted B](./images/offhandSharp_7x3_inverted_B.svg)

![offhand#7x3 inverted C](./images/offhandSharp_7x3_inverted_C.svg)

![offhand#7x3 inverted C#](./images/offhandSharp_7x3_inverted_CSHARP.svg)

![offhand#7x3 inverted D](./images/offhandSharp_7x3_inverted_D.svg)

![offhand#7x3 inverted D#](./images/offhandSharp_7x3_inverted_DSHARP.svg)

![offhand#7x3 inverted E](./images/offhandSharp_7x3_inverted_E.svg)

![offhand#7x3 inverted F](./images/offhandSharp_7x3_inverted_F.svg)

![offhand#7x3 inverted F#](./images/offhandSharp_7x3_inverted_FSHARP.svg)

![offhand#7x3 inverted G](./images/offhandSharp_7x3_inverted_G.svg)

![offhand#7x3 inverted G#](./images/offhandSharp_7x3_inverted_GSHARP.svg)

</details>

<details>
  <summary>The inverted 7x3 minor scales</summary>

![offhand#7x3 inverted Am](./images/offhandSharp_7x3_inverted_Am.svg)

![offhand#7x3 inverted A#m](./images/offhandSharp_7x3_inverted_ASHARPm.svg)

![offhand#7x3 inverted Bm](./images/offhandSharp_7x3_inverted_Bm.svg)

![offhand#7x3 inverted Cm](./images/offhandSharp_7x3_inverted_Cm.svg)

![offhand#7x3 inverted C#m](./images/offhandSharp_7x3_inverted_CSHARPm.svg)

![offhand#7x3 inverted Dm](./images/offhandSharp_7x3_inverted_Dm.svg)

![offhand#7x3 inverted D#m](./images/offhandSharp_7x3_inverted_DSHARPm.svg)

![offhand#7x3 inverted Em](./images/offhandSharp_7x3_inverted_Em.svg)

![offhand#7x3 inverted Fm](./images/offhandSharp_7x3_inverted_Fm.svg)

![offhand#7x3 inverted F#m](./images/offhandSharp_7x3_inverted_FSHARPm.svg)

![offhand#7x3 inverted Gm](./images/offhandSharp_7x3_inverted_Gm.svg)

![offhand#7x3 inverted G#m](./images/offhandSharp_7x3_inverted_GSHARPm.svg)

</details>
