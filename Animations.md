## The @keyframes Rule
When you specify CSS styles inside the `@keyframes` rule, the animation will gradually change from the current style to the new style at certain times.
```css
/* The animation code */

@keyframes example {
    from {background-color: red;}
    to {background-color: yellow;}
}

/* The element to apply the animation to */

div {
    width: 100px;
    height: 100px;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
} 
```
In the example above we have specified when the style will change by using the keywords "from" and "to" 
(which represents 0% (start) and 100% (complete)).

The following example will change the background-color of the `<div>` element when the animation is 25% complete, 50% complete, and again when the animation is 100% complete:
```css
 /* The animation code */
 
@keyframes example {
    0%   {background-color: red;}
    25%  {background-color: yellow;}
    50%  {background-color: blue;}
    100% {background-color: green;}
}

/* The element to apply the animation to */

div {
    width: 100px;
    height: 100px;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
} 
```

The following example will change both the background-color and the position of the `<div>` element when the animation is 25% complete, 50% complete, and again when the animation is 100% complete:
```css
 /* The animation code */
 
@keyframes example {
    0%   {background-color:red; left:0px; top:0px;}
    25%  {background-color:yellow; left:200px; top:0px;}
    50%  {background-color:blue; left:200px; top:200px;}
    75%  {background-color:green; left:0px; top:200px;}
    100% {background-color:red; left:0px; top:0px;}
}

/* The element to apply the animation to */

div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
}
```
## Delay an Animation
The animation-delay property specifies a delay for the start of an animation.
```css
div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
    animation-delay: 2s;
}
```
Negative values are also allowed. If using negative values, the animation will start as if it had already been playing for N seconds.
```css
div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
    animation-delay: -2s;
}
```
## How Many Times an Animation Should Run
```css
/*The following example will run the animation 3 times before it stops:*/

div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
    animation-iteration-count: 3;
}

/*The following example uses the value "infinite" to make the animation continue for ever*/

div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
    animation-iteration-count: infinite;
}
```

## Run Animation in Reverse Direction or Alternate Cycles
The `animation-direction` property specifies whether an animation should be played forwards, backwards or in alternate cycles.

The animation-direction property can have the following values:

   - `normal` - The animation is played as normal (forwards). This is default
   - `reverse` - The animation is played in reverse direction (backwards)
   - `alternate` - The animation is played forwards first, then backwards
   - `alternate-reverse` - The animation is played backwards first, then forwards

The following example will run the animation in reverse direction (backwards):
```css
div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
    animation-direction: reverse;
}
```
The following example uses the value "alternate" to make the animation run forwards first, then backwards:
```css
div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
    animation-iteration-count: 2;
    animation-direction: alternate;
}
```
The following example uses the value "alternate-reverse" to make the animation run backwards first, then forwards:
```css
div {
    width: 100px;
    height: 100px;
    position: relative;
    background-color: red;
    animation-name: example;
    animation-duration: 4s;
    animation-iteration-count: 2;
    animation-direction: alternate-reverse;
}
```
## Specify the Speed Curve of the Animation
The animation-timing-function property specifies the speed curve of the animation.

The animation-timing-function property can have the following values:

   - `ease` - Specifies an animation with a slow start, then fast, then end slowly (this is default)
   - `linear` - Specifies an animation with the same speed from start to end
   - `ease-in` - Specifies an animation with a slow start
   - `ease-out` - Specifies an animation with a slow end
   - `ease-in-out` - Specifies an animation with a slow start and end
   - `cubic-bezier(n,n,n,n)` - Lets you define your own values in a cubic-bezier function

The following example shows the some of the different speed curves that can be used:
```css
#div1 {animation-timing-function: linear;}
#div2 {animation-timing-function: ease;}
#div3 {animation-timing-function: ease-in;}
#div4 {animation-timing-function: ease-out;}
#div5 {animation-timing-function: ease-in-out;}
```
## Specify the fill-mode For an Animation
CSS animations do not affect an element before the first keyframe is played or after the last keyframe is played. The animation-fill-mode property can override this behavior.

The `animation-fill-mode` property specifies a style for the target element when the animation is not playing (before it starts, after it ends, or both).

The `animation-fill-mode` property can have the following values:

   - none - Default value. Animation will not apply any styles to the element before or after it is executing
   - forwards - The element will retain the style values that is set by the last keyframe (depends on animation-direction and animation-iteration-count)
   - backwards - The element will get the style values that is set by the first keyframe (depends on animation-direction), and retain this during the animation-delay period
   - both - The animation will follow the rules for both forwards and backwards, extending the animation properties in both directions

The following example lets the `<div>` element retain the style values from the last keyframe when the animation ends:
```css
div {
    width: 100px;
    height: 100px;
    background: red;
    position: relative;
    animation-name: example;
    animation-duration: 3s;
    animation-fill-mode: forwards;
}

/*The following example lets the <div> element get the style values set by the first keyframe before the animation starts (during the animation-delay period):*/

div {
    width: 100px;
    height: 100px;
    background: red;
    position: relative;
    animation-name: example;
    animation-duration: 3s;
    animation-delay: 2s;
    animation-fill-mode: backwards;
}

/*The following example lets the <div> element get the style values set by the first keyframe before the animation starts, and retain the style values from the last keyframe when the animation ends:*/

div {
    width: 100px;
    height: 100px;
    background: red;
    position: relative;
    animation-name: example;
    animation-duration: 3s;
    animation-delay: 2s;
    animation-fill-mode: both;
}
```

## Animation Shorthand Property

The example below uses six of the animation properties:

```css
div {
    animation-name: example;
    animation-duration: 5s;
    animation-timing-function: linear;
    animation-delay: 2s;
    animation-iteration-count: infinite;
    animation-direction: alternate;
}
```

The same animation effect as above can be achieved by using the shorthand animation property:

```css
div {
    animation: example 5s linear 2s infinite alternate;
}
```
![Image](https://image.ibb.co/fNddMT/Screenshot_20.png)
