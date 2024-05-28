# Getting started with PEPhub

## What is PEPhub?

Just like GitHub allows you to share and edit projects that you are tracking with `git`, PEPhub allows you to share and edit **biological metadata** that is formatted as a **PEP** (a Portable Encapsulated Project). PEPhub allows you to:

- **Upload** your metadata to a central database
- **Edit** your metadata in a web interface
- **Share** your metadata with collaborators

## What is a PEP?

Portable Encapsulated Projects (PEPs) are standard format for biological sample metadata.  A PEP is simply a **yaml** + **csv** file (or just csv) -- the CSV file is a sample table, while the YAML file provides project-level metadata and sample modifiers. PEPs are a common input for running workflows using tools such as [Snakemake](https://snakemake.readthedocs.io/en/stable/), [Common Workflow Language](https://www.commonwl.org/), [Looper](http://pep.databio.org/looper), and other workflow systems. For more details, read the [PEP specification](http://pep.databio.org/spec/simple-example).

## How PEPhub and PEPs work together

PEPhub gives you a central location to store and collaborate on your PEPs. This makes it easier to work together for large or small teams. Instead of relying on local files that you send back-and-forth, PEPhub provides a centralized interface and API that simplifies sharing and collaboration.

In short, PEPs are the standard format for biological metadata, and PEPhub is the platform that allows you to store, edit, and share these PEPs. Through the API, one can easily access and retrieve PEPs for use in workflows and analyses.

## Logging into PEPhub

PEPhub accounts are linked to GitHub. This allows us to leverage GitHub's OAuth system for secure authentication and namespacing. Once you have a [GitHub account](https://github.com/signup), you can log in to PEPhub. Just click the "Login" button in the top right corner of the [PEPhub home page](https://pephub.databio.org). 

![PEPhub login button](../img/login.png)

You will be redirected to GitHub to authorize the PEPhub application. You are now logged in and can upload your first PEP! There are two mains ways to add a PEP to your PEPhub namespace: you can either [upload a PEP directly](#uploading-a-pep), or you can [create a new PEP from scratch](#creating-a-new-pep-from-scratch) using the web interface. This guide will walk you through both methods.

## Uploading a PEP

Navigate to your PEPhub namespace (`https://pephub.databio.org/{github username}`) and click the "Add" button in the top right. Click the "Upload PEP" tab. You will be prompted to select a PEP file from your local machine. Fill in the details about your PEP and then either drag files to the drop zone or click the drop zone to select files from your computer. Click "Submit" to add the PEP to your namespace.

## Creating a new PEP from scratch

Navigate to your PEPhub namespace (`https://pephub.databio.org/{github username}`) and click the "Add" button in the top right. Click the "Blank PEP" tab. Again, fill in the details about your PEP and then you can start filling in the sample table. Click "Submit" to add the PEP to your namespace.

![Submission form for a new PEP](../img/add-pep-form.png)

## Ready to edit your PEP

Once you have uploaded or created a PEP, you can now start using it in pipelines!

## Editing a PEP

Editing a PEP is easy; just make changes in the table and click `Save` when you are finished.

## Sharing your PEP

By default, new PEPs are set to public access. This means anyone who has the link can read your table. You can share it by simply sharing the URL. You can restrict this by marking it as `private` in the Project edit menu.

If you want to give another user *write* access, then you'll need to do a bit more work. Since PEPhub user permissions are inherited directly from GitHub, you'll use GitHub to manage these. You should transfer the PEP into an organization where both users are public members. This will give both users write access to the PEP.









