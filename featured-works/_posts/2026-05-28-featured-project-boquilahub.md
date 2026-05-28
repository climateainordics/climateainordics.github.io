---
title: "Featured project: BoquilaHUB - SOTA AI models for biodiversity"
people:
- José Díaz
image: /images/posts/boquilahub-img2.png
summary: "BoquilaHUB is an open-source desktop application that makes state-of-the-art AI for biodiversity accessible without complex setup or coding. It enables researchers to efficiently process large-scale camera trap and bioacoustic data using leading models like SpeciesNet and Perch 2. It also supports easy local deployment and shared GPU access, helping democratize AI tools for conservation worldwide."
---

**Authors:** José Díaz

**Project website:** [https://github.com/boquila/boquilahub/](https://github.com/boquila/boquilahub/)

# Biodiversity data

A lot of biodiversity monitoring uses methods that produce massive amounts of data. Camera traps, bioacoustics, live cameras, etc. It all can turn into a job that requires people working full-time just going through many files.

Luckily, many innovations in AI have been helpful to automate part of this job. But the software stack is behind; using AI can require many different packages, complicated installations, incompatible versions. It can turn into a nightmare fast.

# How BoquilaHUB is solving it

BoquilaHUB is an open-source desktop application that runs on Windows and Linux. You can use it to run AI models for biodiversity use cases like camera trap processing and audio species classification. You can select from many models that are officially supported,
or you can bring your own and they can just run (as long as the core architecture is supported).

It currently runs many SOTA models—SpeciesNET, which is state-of-the-art for camera trap species classification; Perch 2, which leads biodiversity audio classification (birds, insects, frogs, mammals, etc); and much more, including even wildlife detection or
bug segmentation (useful for counting under the microscope).

![](/images/posts/boquilahub-img1.png)

On a powerful computer, you could easily process a few terabytes of camera trap data in a single night, with SOTA AI predictions.

# The goal

BoquilaHUB wants to democratize access to AI models. It shouldn't require Python knowledge to run a SOTA model that can be helpful for nature. One of the things we've seen from our users, many of them in developing countries, is that it's not super common
to have access to a computer with an Nvidia GPU (that can run AI fast). So we also make it extremely easy to use BoquilaHUB to deploy a REST API endpoint that can allow other users in your local network to use your BoquilaHUB instance.
For example, if an office of researchers has only one good computer with a powerful GPU, it's very easy for that computer to serve SpeciesNet to 20 other computers, everyone just needs to make just a few clicks and it's done.

# What's next

Ironically, AI predictions can also produce a lot of data, and this new data needs to be managed. BoquilaHUB will be providing tools to manage and understand AI predictions better—edit, transform, visualize, or maybe even automatically sort them with another AI.

Plus, better platform support, better GPU support, and more.
