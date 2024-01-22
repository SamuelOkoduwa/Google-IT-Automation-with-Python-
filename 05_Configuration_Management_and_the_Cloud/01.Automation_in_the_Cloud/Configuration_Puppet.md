***

<h1>Automation in the Cloud</h1>

***

<h2>Objectives</h2>

- Understand the definition of working at scale and how automation is an essential tool
- Understand the difference between unmanaged and managed configuration systems
List the benefits of infrastructure as code
- Understand what Puppet is and how Puppet facts work
- Understand what Puppet resources and classes are
- Define the principles of configuration management

***

Cloud Computing
---

Clouds are not the ones that float through the sky, but computer services that run in a data center or remote servers that we access over the Internet. These clouds have different service types, from a bare bones environment that gives you the computing power to run your own software with your own configuration settings, to those that deliver a whole application or program to a user, such as easy to use email solutions like Gmail, storage solutions like Google Cloud, or productivity suites like Google Workspace. 

Virtual machine (VM), are set up to serve our web app, and would stay updated via Puppet. A single VM can be useful for small operations with lower technical requirements, but as technical requirements increase, an organization will need to deploy more and larger cloud solutions. Luckily, it’s easy to scale in the cloud. So we turned that single VM into a customized VM template that could be used to clone that VM as many times as we want, so scaling our cloud deployments would be easy. 

When we had a VM template, we looked at different ways to interact with the platform. We saw how both the web interface and the command line tool can be used to create VMs in the cloud, modify their configuration, and control other things, using tools which are very effective at a small or medium scale. 

At a large scale, you’ll need to automate cloud deployments even further using orchestration. We looked at how tools like Terraform allow us to define our cloud infrastructure as code, which can give us a lot of control over things like how the infrastructure is managed, and how changes are applied. Orchestration lets us combine the power of infrastructure as code with the flexibility of cloud resources. 

Then it was time to look at some of the options for building software for the cloud. FIrst, we looked into the different types of storage available, and what to consider when deciding which storage solution to use. These considerations include how we want to request data from storage, and how fast we want to be able to access the requested data.

Maybe the number one reason for using cloud computing is how much computing power is available across many servers. But in order to distribute our service evenly across however many instances we have available, we use load balancing. We talked about the different methods load balancers use to distribute the workload, and how they can monitor server health to avoid sending requests to unhealthy servers. 

There is no doubt that computing methods are constantly changing, and this happens pretty fast. We talked about how change management allows us to make changes in a safe and controlled way. We looked at how continuous integration (CI) can build and test code every time there is a change, and how continuous deployment (CD) can automatically control the deployment of new code to a specified set of rules. And we talked about different environments where new code could be tested before being pushed to production. 

The limitations encountered when running services in the cloud are not the same as limitations when running services on physical machines, and you should take time to understand the limitations of any cloud solution you may choose. 

***
Practice Quiz: Cloud Computing
===

***

1. When we use cloud services provided to the general consumer, such as Google Suite or Gmail, what cloud deployment model are we using?
*Ans => Public Cloud*

2. What is a container
*Ans => A virtualized environment containing applications and configurations that can run quickly and reliably on any computing environment*

3. Select the examples of Managed Web Application Platforms. (Check all that apply)
*Ans => 
Google App Engine
Amazon Elastic Beanstalk
Microsoft App Service*

4. When a company solely owns and manages its own cloud infrastructure, what type of cloud deployment model are they using?
Ans => Private cloud

5. Which "direction" are we scaling when we add RAM or CPU resources to individual nodes?
Ans => Vertical


***
Practice Quiz: Managing instances in the cloud
---
***
1. What is templating
*Ans => The process of capturing the entire system configuration to enable us to reproduce virtual machines*

2. Why is it important to consider the region and zone for your cloud service?
*Ans => To ensure bandwidth and reliability for users*

3. What option is used to determine which OS will run on the VM?
*Ans => Boot disk*

4. When setting up a new series of VMs using a reference image, what are some possible options for upgrading services running on our VM at scale?
*Ans => 
Create a new reference image each update,
Use a configuration management system like Puppet*

5. When using gcloud to manage VMs, what two parameters tell gcloud that a) we want to manage our VM resources and b) that we want to deal with individual VMs? (Check two)
*Ans => 
Compute
Instances*

***
Practice Quiz: Automating Cloud Deployments
---
***
1. In order to detect and correct errors before end users are affected, what technique(s) should we set up?
*Ans => Monitoring and alerting*

2. When accessing a website, your web browser retrieves the IP address of a specific node in order to load the site. What is this node called?
*Ans => Entry Point*

3. What simple load-balancing technique just assigns to each node one request at a time?
*Ans => Round Robin*

4. Which cloud automation technique spins up more VMs into instance groups when demand increases, and shuts down VMs when demand decreases?
*Ans => Autoscaling*

5. Which of the following are examples of orchestration tools used to manage cloud resources as code? (Check all that apply)
*Ans =>
Terraform,
CloudFormation,
Azure Resource Manager*

***
Practice Quiz: Building Software for the Cloud
---
***
1. What is latency in terms of Cloud Storage?
*Ans => The amount of time it takes to complete a read or write operation.*

2. Which of the following statements about sticky sessions are true? (Select all that apply.)
*Ans =>
All requests from the same client always go to the same backend server;
They should only be used when needed;
They can cause problems during migration.*

3. If you run into limitations such as rate limits or utilization limits, you should contact the Cloud provider and ask for a ___
*Ans => Quota increase*

4. What is the term referring to everything needed to run a service?
*Ans => Environment*

5. What is the term referring to a network of hosts spread in different geographical locations, allowing ISPs to be as close as possible to content?
*Ans => Content Delievery network*

