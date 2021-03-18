# RoamWear
RoamWear is a personal knowledge management system, similar to [Roam Research](https://roamresearch.com/), made specifically for Android smartglasses such as the Vuzix Blade. (Work in progress)

![Diagram showing how the app could be used](https://i.imgur.com/N3TSYsQ.png)

## Introduction

The ultimate goal of this application is to provide the ability to take, organize, and retrieve notes using the Zettelkasten method on a pair of **smartglassess** while on-the-go, or for situations where you can't access a smartphone or computer. With smartglasses, it gives users hands-free access to their information. Paired with a wearable keyboard such as the open-source [Palm Pro BLE Keyboard](https://www.parallelinnov.com/palm-pro-wearable-keyboard/)([GitHub](https://github.com/parallelinnovation/Palm-Pro-Wearable-Keyboard)), it allows for the ability to take notes and control the application as well. This program is aimed to have a simple UI that can capture information in the same powerful format that personal knowledge management systems such as Roam Research or Obsidian uses. It should store files as Github-flavoured markdown so that data can be interchangable across these platforms. 

## Device Specifications 

The [Vuzix Blade](https://www.vuzix.com/products/blade-smart-glasses-upgraded) will be used as the platform for the first version. It has a display resolution of 480x480 and runs on an ARM Cortex-A53 processor. The OS is a slightly modified Android Lolipop v5.1. 

## Proposed Design

Vuzix provides detailed UX design guidlines and other resources for developing on the Blade in their developer section. You can easily sign up [Here](https://www.vuzix.com/Developers) to become a Vuzix developer. 

I plan on using Python and [KivyMD](https://github.com/kivymd/KivyMD). 
So far, it has 3 main screens: The home screen which desplays recent files, the editor, and the finder screen to search files. In the editor, there is also a bottom screen that opens up to show the backlinks. I plan on adding an inline auto-suggest feature to the editor that prompts when you start typing the start of a link "[[". I still need to figure out how to navigate the selection using arrow and keyboard controls instead of using touch buttons, but for now I'm using buttons to get a structure going. The finder screen needs work to comfortablly search with. There will also be an additional settings screen where I plan on having an option to save the database as markdown files.


As a public Roam API is not currently available, the plan is to store the files locally on the device for now. 
