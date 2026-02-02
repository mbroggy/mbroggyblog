---
title: 'Posting Hugo Entries to Mastodon'
date: 2025-07-09T20:45:53-04:00
draft: false
categories:
- blog
- tech
description: Testing a Huginn workflow, snagging Hugo posts via RSS to post to Mastodon...
stage: seed
---
Leveraging a couple of articles and a friend's suggestion of Huginn, this might actually work...
<!--more-->
I started using Hugo - as I've attempted a few  blogs and sites over the years - to journal various projects and hobbies or capture thoughts and the like over the years...  At the same time, I had wanted to get away from the social media behemoths and get back to using Mastodon (...or seriously ever start).

If I couldn't keep on Hugo, though, and there wasn't a (known) critical mass on Mastodon...well, just looking at the infrequency of my posts on either tells the story.

But if I could post to Hugo and get it to Mastodon with little to trouble...*and* make it a nerdy project along the way?

Enter Huginn. I had beat my head against it before by installing it as a docker container on my QNAP (which worked right out of the box) and on unRAID (which didn't) and since I didn't keep the QNAP around and it wasn't working on unRAID, my ADHD brain ran off to something else it likely wouldn't finish.

Enter Huginn *again*, after I decided to pin my brain still on it for a few hours and it turned out that the failure on unRAID was a permissions thing.  I *should* figure it out properly and not just alter the permissions on the share external to the container...but here we are.

I won't call out C *directly* but also [Interfacing Huginn with Mastodon](https://drwho.virtadpt.net/archive/2018-08-20/interfacing-huginn-with-mastodon/) helped with much of the set up.

So...fingers crossed, this might work or it might not...
