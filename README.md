# RoamWear
RoamWear is a personal knowledge management system, similar to [Roam Research](https://roamresearch.com/), made specifically for Android smartglasses such as the Vuzix Blade. (Work in progress)

![Diagram showing how the app could be used](https://i.imgur.com/N3TSYsQ.png)

## Introduction

The ultimate goal of this application is to provide the ability to take, organize, and retrieve notes using the Zettelkasten method on a pair of **smartglassess** while on-the-go, or for situations where you can't access a smartphone or computer. With smartglasses, it gives users hands-free access to their information. Paired with a wearable keyboard such as the open-source [Palm Pro BLE Keyboard](https://www.parallelinnov.com/palm-pro-wearable-keyboard/), it allows for the ability to take notes and control the application as well. This program is aimed to have a simple UI that can capture information in the same powerful format that personal knowledge management systems such as Roam Research or Obsidian uses. It should store files as Github-flavoured markdown so that data can be interchangable across these platforms. 

## Device Specifications 

The [Vuzix Blade](https://www.vuzix.com/products/blade-smart-glasses-upgraded) will be used as the platform for the first version. It has a display resolution of 480x480 and runs on an ARM Cortex-A53 processor. The OS is a slightly modified Android Lolipop v5.1. 

## Proposed Design

Vuzix provides detailed UX design guidlines and other resources for developing on the Blade in their developer section. You can easily sign up [Here](https://www.vuzix.com/Developers) to become a Vuzix developer. 

I plan on using Python and [KivyMD](https://github.com/kivymd/KivyMD) instead of Android Studio, only because my programming knowledge is limited to python at the moment. I'm not sure yet if this will even work for developing on the Blade, since I made a simple test app, tried to install it on the Blade, and it just crashes. If I can't get it to work with Python, I guess I need to learn Java and xml. Kotlin is also a possibility. 

As a public Roam API is not currently available, the plan is to store the files locally on the device for now. 
