# 1. Module Intro

Hi, my name is Hemant, and I'm a senior principal training lead at Oracle University. I welcome you to this module. To begin with, in this module, we will discuss OCI AI services. Next to that, we will also discuss OCI machine learning services. Following that, we will also discuss OCI AI infrastructure. And we will end with responsible AI principles. So let's begin.

# 2. AI Services Overview

In this lesson, I will take you through an overview of OCI AI services. Oracle has been focusing on bringing to the enterprise at every layer of our stack. It all begins with data and infrastructure layers. OCI AI services consume data, and AI services in turn are consumed by applications. This approach involves extensive investment from infrastructure to SaaS applications. Generative AI and massive scale models are the more recent steps. Oracle AI is the portfolio of cloud services for helping organizations use the data they may have for the business-specific uses.

Business applications consume AI and ML services. The foundation of AI services and ML services is data. AI services contain prebuilt models for specific uses. Some of the AI services are pretrained, and some can be additionally trained by the customer with their own data. AI services can be consumed by calling the API for the service, passing in the data to be processed, and the service returns a result. There is no infrastructure to be managed for using AI services. In this lesson, the focus is on OCI AI services.

OCI AI services provide multiple methods for access. The most common method is the OCI Console. The OCI Console provides an easy-to-use, browser-based interface that enables access to notebook sessions and all the features of all the data science, as well as AI services. Rest API, the Rest API provides access to service functionality but requires programming expertise. An API reference is provided in the product documentation.

Language SDK OCI also provides programming language SDK for Java, Python, TypeScript/JavaScript, Net, Go, and Ruby. The command line interface provides both quick access and full functionality without the need for scripting. Let us see what type of OCI services are available.

OCI AI services is a collection of services with prebuilt machine learning models that make it easier for developers to build a variety of business applications. The models can also be custom trained for more accurate business results. The different services provided are Digital Assistant, Language, Vision, Speech, Document Understanding. Let us explore each one of these services.

OCR Language allows you to perform sophisticated text analysis at scale. Using the pretrained and custom models, you can process unstructured text to extract insights without data science expertise. Language services are provided by pretrained models, custom models, and text translation. Pretrained models include language detection, sentiment analysis, key phrase extraction, text classification, named entity recognition, and personal identifiable information detection. Custom models can be trained for named entity recognition and text classification with domain-specific data sets.

In text translation, neural machine translation is used to translate text across numerous languages. Using OCR Vision, you can upload images to detect and classify objects in them. Pretrained models and custom models are supported. In Image Analysis, pretrained models perform object detection, image classification, and optical character recognition.

In image analysis, custom models can perform custom object detection by detecting the location of custom objects in an image and providing a bounding box. The custom image classification builds a model to identify objects and scene-based features in an image. The OCI Speech service is used to convert media files to readable texts that's stored in JSON and SRT format. Speech enables you to easily convert media files containing human speech into highly exact text transcriptions.

Using OCI Document Understanding you can upload documents to detect and classify text and objects in them. You can process individual files or batches of documents. And OCR Document Understanding can detect and recognize text in a document. In text extraction, Document Understanding provides the word level and line level text and the bounding box coordinates of where the text is found.

In Key Value Extraction, Document Understanding extracts a predefined list of key value pairs of information from receipts, invoices, passports, and driver IDs. In Table Extraction, Document Understanding extracts content and tabular format, maintaining the row and column relationship of cells. In Document Classification, the Document Understanding classifies documents into different types.

Oracle Digital Assistant is a platform that allows you to create and deploy digital assistants, which are AI-driven interfaces that help users accomplish a variety of tasks with natural language conversations. When a user engages with the Digital Assistant, the Digital Assistant evaluates the user input and routes the conversation to and from the appropriate skills. Digital Assistant greets the user upon access, upon user request, lists what it can do, and provide entry points into the given skills. It routes explicit user requests to the appropriate skills. And it also handles interruptions to flows and disambiguation. It also handles requests to exit the bot. Thanks for listening.

# 3. ML Services Overview

Hello and welcome to this lesson on ML Services Overview. As we have already seen, Oracle is this portfolio of cloud services for helping organizations take advantage of all data for the next generation of scenarios. The foundations of AI services and ML services layer is data.

Obviously, AI and machine learning work on data and required it. The top layer of this diagram is applications and loosely refers to all the ways AI is consumed. This could be an application, a business process, or an analytics system. Between the application and data layer, you see two groups here-- the AI services on the top and the machine learning services on the bottom.

We have already seen about AI services in the lesson titled AI Services Overview. In this lesson, we are going to primarily focus on OCI Data Science as a part of machine learning services. So what is Oracle Cloud Infrastructure Data Science? OCI Data Science is the cloud service focused on serving the data scientists throughout the full machine learning life cycle, with support for Python and open source.

As you can see by icon in this graphic, the service has many features, such as model catalog, projects, JupyterLab Notebook, model deployment, model training, management, model explanation, open-source libraries, and AutoML. There are three core principles of OCI Data Science. The first one, accelerated. The first principle is about accelerating the work of the individual data scientist. OCI Data Science provides data scientists with open-source libraries, along with easy access to a range of compute power, without having to manage any infrastructure. It also includes Oracle's own library to help streamline many aspects of their work.

The second principle is collaborative. It goes beyond an individual data scientist's productivity to enable data science teams to work together. This is done through the sharing of assets, reducing duplicative work, and putting reproducibility and auditability of models for collaboration and risk management.

Third is enterprise grade. That means it's integrated with all the OCI security and access protocols. The underlying infrastructure is fully managed. The customer does not have to think about provisioning compute and storage. And the service handles all the maintenance, patching, and upgrades so user can focus on solving business problems with data science.

So having seen the core principles, let's drill down a bit more into the specifics of OCI Data Science. So again, what is OCI Data Science? It's a cloud service to rapidly build, train, deploy, and manage machine learning models. Whom does it serve? It serves data scientists and data science teams throughout the full machine learning life cycle, with support for Python and open source.

Where it is being used-- users work in a familiar JupyterLab Notebook interface, where they write Python code. And how it is used-- so users preserve their models in the model catalog and deploy their models to a managed infrastructure.

Some of the important product terminology of OCI Data Science are projects. The projects are containers that enables data science teams to organize their work. They represent collaborative workspaces for organizing and documenting data science assets such as notebook sessions and models.

Note that tenancy can have as many projects as needed without limits. Now this notebook session is where the data scientists work. Notebook sessions provide a JupyterLab environment with preinstalled open-source libraries and the ability to add others.

Notebook sessions are interactive coding environment for building and training models. Notebook sessions run in a managed infrastructure, and the user can select CPU or GPU, the compute shape, and amount of storage without having to do any manual provisioning.

The other important feature is Conda environment. It's an open-source environment and package management system and was created for Python programs. It is used in the service to quickly install, run, and update packages and their dependencies. Conda easily creates, saves, loads, and switches between environments in your notebook sessions.

The next one is Accelerated Data Science SDK. Oracle's Accelerated Data Science, ADS, SDK is a Python library that is included as part of OCI Data Science. ADS has many functions and objects that automate or simplify the steps in the Data Science workflow, including connecting to data, exploring and visualizing data, training a model with AutoML, evaluating models, and explaining models. In addition, ADS provides a simple interface to access the Data Science service, Model Catalog, and other OCI services, including Object Storage.

The next one is models. You already know what a model is. Models define a mathematical representation of your data and business process. You create models in notebooks, sessions, and side projects.

The next terminology is Model Catalog. The Model Catalog is a place to store, track, share, and manage models. The Model Catalog is a centralized and managed repository of model artifacts.

A stored model includes metadata about the provenance of the model, including Git-related information, and the script-- all notebook used to push the model to the catalog. Models stored in the Model Catalog can be shared across members of a team, and they can be loaded back into a notebook session.

The next one is model deployments. Model deployments allow you to deploy models stored in the Model Catalog as HTTP endpoints on managed infrastructure, deploying machine learning models as web applications, HTTP API endpoints. Serving predictions in real-time is the most common way to operationalize models. HTTP endpoints or the API endpoints are flexible and can serve requests for the model predictions. The last one which we are going to see here is jobs. Data Science jobs enable you to define and run a repeatable machine learning tasks on fully managed infrastructure.

# 4. AI Infraestructure

Graphics Processing Unit, or GPU, is a very important component of AI infrastructure. Let us see what is a GPU and why GPU is required. Machine learning and AI workloads need lots of repetitive calculations to be made on huge amount of data, especially for model training and inference as well. GPU is a piece of hardware that is incredibly good in certain type of calculations.

Parallel computing on GPU is designed to run many processes at the same time. GPU has thousands of lightweight cores, all working on their share of data in parallel. This gives them the ability to crunch through extremely large data sets at tremendous speed. GPU can process many inference tasks in parallel, leading to significantly higher throughput compared to CPU. This is especially useful for batch processing or serving multiple requests simultaneously.

Modern GPUs are optimized for deep learning frameworks like TensorFlow, PyTorch, and ONNX Runtime. These frameworks leverage GPU-specific libraries to accelerate computations. Now let us take a look at a few NVIDIA GPU.

A100 was introduced in 2020 and uses Ampere architecture. Tensor cores are crucial components of this architecture. Tensor cores can perform multiple fuse, multiply, accumulate operations in a single clock cycle, and hence, accelerate deep learning workloads.

The Hopper architecture was introduced with H100 in 2022 and is a dedicated transformer engine designed to optimize the performance of transformer models. H200 was introduced in 2024 and is like H100, but with more memory. Blackwell architecture is designed to accelerate large-scale AI models.

This aligns with the growing focus on the LLM and is introduced in 2025. The NVIDIA Grace CPU is a breakthrough processor and is designed for modern data centers running AI Cloud and HPC applications. NVIDIA GB200, Grace Blackwell and L4 superchip unlocks performance through for Blackwell GPU unified with two base CPU and is introduced in 2025.

To support a wide range of small, medium, and large use cases, OCI is broadening its lineup of GPU compute OCI compute with a 10,800 H100N. L40 GPU is now generally available. Also, we are now taking orders for OCI compute with H200 B200 GPUs and GB200 superchips, and these will be generally available in 2025. We are also taking orders for superclusters built using these GPU.

Beginning with H200, we can go 4X performance of H100 superclusters. And with B200 and GB200, we can go APEX performance of H100 for AI workloads. Here is how we can use OCI AI infrastructure through OCI Data Science for training and deployment of LLM.

We can directly deploy popular LLM to the VM or bare metal instances powered by GPU through OCI Data Science AI Quick Actions. We can also fine-tune the base models further and then deploy the custom models for inference through OCI Data Science Add Quick Actions. Currently, you can register any model supported by virtual LLM, next generation inference, or text-embedding inference containers in AI quick actions. Thanks for listening.

# 5. GPUs and Superclusters in OCI

Welcome to the First Principles video and blog series where we talk about various architectural aspects behind OCI services. At OCI, we take a lot of pride in delivering the maximum performance possible for the least cost possible to customers.

Remote DMA, or RDMA, as we call it, has been a core technology behind many OCI services pretty much from the beginning. And we actually recently released a video blog talking about various architectural aspects, historical aspects right from the beginning about why we decided to invest in RDMA and the various products that use RDMA and various trade-offs associated with that.

RDMA is essentially, in a nutshell, is a technology that allows for data transfer or network communication that bypasses CPU, goes from one machine to another without any CPU interference. And this allows things like GPUs to communicate at extremely low latency, high bandwidth with low overhead from a CPU perspective.

And this has actually been a foundational building block for our database services, such as ExaCS and Autonomous Database services and as well as for HPC workloads, as well as GPU workloads. And a few years back, we decided to make a strategic bet on Rocky. Rocky stands for RDMA or converged ethernet. So right now, we essentially have an ethernet fabric that essentially enables Rocky. And our HPC workloads, GPU workloads, as well as database workloads all run on-- leverage that and run on top of it.

In the last Cloud World, we announced a strategic partnership with NVIDIA around GPU workloads. And in that context, we've been talking to customers as well as NVIDIA. And it's become very clear that there is a clear demand for very high scale GPU workloads that spans maybe thousands or maybe even tens of thousands of GPUs that can essentially run within a single RDMA network, if you will.

It's essentially like a Supercluster that essentially supports RDMA. And in order to cater that workload, we went back and decided to make some engineering and architectural design enhancements to roll out what we call as RDMA Supercluster that is designed to support very large number of GPUs. To talk about some of the architectural aspects of our Supercluster, we have with as again Jack, who is the lead architect for RDMA networking. Welcome, Jack.

Thank you, Pradeep. I'm here to represent the team.

As always. All right, so tell us a little bit more about the Superclusters.

Yes, so let's take a look at schematic here. This is probably a high level drawing. So what we're showing here is we're showing two GPU nodes at the bottom where each node is comprised of eight NVIDIA A100 class of GPUs that are interconnected using NVIDIA's NVLinks. This is NVLinks.

And the GPU nodes themselves connect to what we call the network fabric. And the way to think about this is network fabric provides a nonblocking interconnect between all the GPUs, meaning the fabric can provide all the benefit that all the GPU nodes need. And in this case, each GPU node connects to the fabric at 1.6 terabits per second or 1,600 gigabits per second. That's like the high level view. Now let's take a look at what the fabric looks like.

So this is like for every GPU that's 200 gigabits per second?

Correct. Each of the GPU gets 200 gigabits of proportional bandwidth because there's a total of 1.6 G.

Right. And it's fully operational. And it's nonblocking in the sense that any GPU in the fabric can talk to any other GPU fabric at a time.

At the same time, yes.

Good observations.

So looking at-- this is the next-level picture of the fabric. So here we look at what the fabric looks like. Now, we use the word Supercluster. By Supercluster what we mean is, it's much larger than an existing cluster network. In particular, we have a concept of blocks. So there's block number one here and block number n here.

Each of the blocks have two tiers of what we call the Clo fabric. Clo is a particular kind of network design. This is a three-tier Clo network. So this network, we plan to scale to tens of thousands of GPUs. And we can envision designs and scale over 100,000 GPUs as well.

Got it. So this is essentially a three-tier Clo network. And so thinking about this, let's say a GPU all the way over here in the block number one wants to talk to the GPU at the very right side of the n, the GPU block, if you will. Well, I can imagine there's going to be additional network latency because of this three-tier Clo design correct in terms of the number of hops. So how do you actually manage that?

Very good point. So you observed correctly. Because this Supercluster is so large, we're talking tens of thousands GPUs. Potentially, we can talk over 100,000 GPUs. That's a lot of GPUs. And just physical constraints, as in power and space, would mean, we have a long what's called a cable distance.

So the worst-case latency in this case, we're talking around 20 microseconds round trip. And as we previously noted in the other blog, the latency within a block is about 6.5 microseconds round trip. So latency has gone up, but still we're talking not very high latency.

Now, in order to account for that higher latency, what we're doing is we have-- because this is QOS-enabled network, as we talked about in the other blog, we have made sure that the switches and the silicon and the chipsets we chose have the right amount of buffering. And we have made sure to allocate the right amount of buffers to the queue that the NLGPU workloads would use. So we have taken care of the higher worst-case latency here.

Got it. So this is not just like a regular three-tier Clo which has been around for a while. It's essentially something that's designed so that we can do lossless networking, if you will, using higher buffers that are specifically tuned across all these devices in order to make this three-tier Clo Supercluster work in conjunction with RDMA.

Very true. You used the right word, the word that I missed. The operating word is lossless. So this is a lossless RDMA network. And lossless networking means the switches don't drop packets. And they have intelligent congestion notification system built into it to avoid packet loss. And all of that still applies. But we just made sure we account for the worst-case higher latency, so the packets are never dropped still.

Cool. So that's great for-- 20 microseconds is still pretty great compared to any other virtualized networking, if you will. Typically, that's like an order of magnitude better than a cross AD virtual network that we might find. But still there are workloads that are extremely sensitive to latency. And they still may want the 6, 7 microsecond latency, How do we deal with that in the Supercluster.

Very good point. Firstly, as you said, the latency, the worst-case latency we talked about is still 10 to 20 times lower than what you would typically experience in a cloud network. But in order to support workloads that need lower latency or that don't really need the scale we're talking about here, imagine you have a small GPU cluster. You don't need tens of thousands of GPUs. You need maybe 1,000 GPUs, or an HPC workload, or an Oracle database workload that maybe doesn't need that larger scale or really cares about low latency.

So what we do for those workloads is we have a control plane that figures out where to deploy a customer's workload. And it takes into account this latency. So if you have a small-enough workload that fits in a cluster, it would only be deployed in what we call a single block. So you would then experience--

Like a HPC or a database cluster workloads essentially go into a single block.

Exactly, or even a smaller workload. It'll go in a single block. And it'll experience the lower latency. So we struck the balance between scale and latency using what we call placement.

Yeah, makes sense. Cool. How about GPU workloads, though? Let's say they actually span multiple of these blocks. Are they essentially going to have to deal with the 20 microsecond latency all the time?

Very good point. And the answer is not all the time. And let's take a look at how we do that. In fact, we believe it's an innovative thing we've done. So as we talked about in the other blog, we have this thing called network locality hints. So we have a service that provides network locality information to the customers and help them build, for example, their GPU topology, their ML topology to take advantage of that.

So let's take a look at that here. So here we're showing a workload that has eight hosts behind four different top of the rack switches in two different blocks. So this is one block. That's another block. Now, if the workload didn't know anything about locality, then any GPU could be talking to any other GPU at the same time. And you could have relatively higher latency. Still lower numbers but higher than what it needs to be.

So what we've done is we make network locality transparent to the customer. We make that information available to the customer. And what in this case the customer has done is they've interconnected their GPUs in a way where two GPUs on the top of the rack switch, half of their traffic stays local to the top of the rack switch.

For GPUs within the block, something like 85% of the traffic stays local. If you look at all these links, they're local to the block. Just occasionally, some of these links go across blocks. And what this means is most of the time, most of the traffic has really low latency.

Occasionally, some of the traffic has that 20-ish microsecond latency. But the end result is on average, your latency is much lower. In fact, half of the traffic has even less than 6.5 microseconds of latency because they're local to the top of the rack switch. So this is what we call network locality or placement hints.

Got it. And if there are a lot of the traffic is actually constrained within a tour or a block, that also helps reduce flow collisions at many levels of these, the three--

Very good observation. So we got a very nice side benefit, which is customers get really high throughput because this thing called flow collision, which is a common phenomena in all networks where two flows could collide on a single link. The probability of that is much reduced. So you not only get lower latency, you get higher throughput.

Got it. Cool. Well, to summarize, essentially the Supercluster is a three-tier cloud network. But it's a whole bunch of optimizations?

Correct.

The three big things that I think I heard were, one, we have buffers that are tuned for the approximate latency diameter in the network itself so that we can actually preserve the lossless aspect of the Supercluster.

Correct.

And second, we have placement mechanism in our control plane where when you launch GPU nodes or maybe database nodes or whatever, they actually tend to as much as possible be placed within the same block or maybe even within the same tour to reduce the latency as well as to decrease the probability of flow collisions across the network--

That's higher throughput.

--and which results in higher throughput. And then the third, we have even for workloads that actually span multiple blocks or tours. We actually have placement hints that can be passed down to the orchestration mechanism like the GPU workloads where the algorithms can essentially use the locality within the orchestration itself to limit the traffic within tours or maybe blocks as much as possible, reducing the latency as well as reducing the probability of flow collision.

Correct. You said it better than I could have. Thank you.

Cool. Thank you, Jack, appreciate--

My pleasure.

--your time.

# 6. Responsible AI

In this lesson, we will learn about responsible AI. We are increasingly using AI in our day-to-day work. But can we trust AI? For example, do we trust self-driven cars completely? Or do we accept AI-driven disease diagnosis without a second opinion?

The guiding principles for AI to be trustworthy are AI should be lawful, complying with all applicable laws and regulations. AI should be ethical. That is, it should ensure adherence to ethical principles and values that we uphold as humans. And AI should be robust both from a technical and social perspective because even with the good intentions, AI systems can cause unintentional harm.

AI systems do not operate in a lawless world. A number of legally binding rules at national and international level apply or are relevant to the development, deployment, and use of AI systems today. The law not only prohibits certain actions, but also enables others like protecting rights of minorities or protecting environment. Besides horizontally applicable rules, various domain-specific rules exist that apply to particular AI applications, for instance, the medical device regulation in the health sector.

So let us discuss human ethics and fundamental rights. Human dignity encompasses the idea that every human being possesses an intrinsic worth, which should never be diminished or compromised. Systems should therefore be developed in a manner that respects and protects humans' physical and mental integrity. Freedom of the individual means a commitment to protect the freedom of expression and the right to private life and privacy.

AI systems should serve to maintain and foster democratic processes and respect the choices of individuals. AI systems must not undermine democratic processes or democratic voting systems. In AI context, equality entails that the systems operations cannot generate unfairly biased outputs. And while we adopt AI, citizens' rights should also be protected.

So our AI ethics derived from these. There are three main principles. AI should be used to help humans and allow for oversight. It should never cause physical or social harm. Decisions taken by AI should be transparent and fair and also should be explainable.

As it follows, the ethical principles as responsive AI. So if we map the ethical principles to responsible AI requirements, these will be like AI systems should follow human-centric design principles and leave meaningful opportunity for human choice. This means securing human oversight. AI systems and environments in which they operate must be safe and secure. They must be technically robust and should not be open to malicious use.

The development and deployment and use of AI systems must be fair, ensuring equal and just distribution of both benefits and costs. AI should be free from unfair bias and discrimination. Decisions taken by AI to the extent possible should be explainable to those directly and indirectly affected. Let us quickly see what is typical responsible AI implementation process looks like.

First, a governance needs to be put in place. Second, develop a set of policies and procedures to be followed. And once implemented, ensure compliance by regular monitoring and evaluation. Typical roles that are involved in the implementation cycles are developers, deployers, and end users of the AI.

One of the key challenges in using AI in health is ensuring its fairness and lack of bias. AI systems are only as good as the data that they are trained on. If that data is predominantly from one gender or racial group, the AI systems might not perform as well on data from other groups.

Another challenge in using the AI in health is ensuring that it's transparent and explainable. AI systems often make decisions based on complex algorithms that are difficult for humans to understand. As a result, patients and health care providers can have difficulty trusting the decisions made by the AI, as systems must be regularly evaluated to ensure that they are performing as intended and not causing harm to patients. Thanks for watching.

# 7. Demo: Data Science

Since we have talked about OCI Data Science service briefly and now familiar with related features and terms, in this demo on OCI Data Science service, I will replicate the machine learning demo shown earlier in our data science environment. You can sign up for an Oracle account and play with Oracle Data Science service. We won't discuss setting up policies and workspaces. For that, I encourage all of you to take OCI Data Science Professional course, which should be your next stop in your AI and ML journey, especially with Oracle.

Again, Data Science is a fully managed platform for teams of data scientists to build, train, deploy, and manage machine learning models using Python and open source tools. It's available in the Machine Learning stack under Analytics and AI. You can select Data Science from this Machine Learning stack under Analytics and AI.

Once you click on this Data Science, it will bring you to this particular page. You can click here and see some of the basic prerequisites needed. And you can already see that I haven't already created project in active state. You can click on Create Project, select your compartment, give project name and description, and then click on this Create button. And this should create a project for you.

After clicking on this active project here, this is how the page will look. You can see multiple notebook sessions which you would have created, their state, compute, shape, network, and endpoint details. In the left pane, apart from notebook sessions, you have an option to view and create jobs. This is how it looks. Pipelines, Models. You can see multiple models which I had created earlier, and again, model deployments. Let's go back to notebook session.

Now to create a notebook session, click on Create Notebook Session. You can then select compartment. Provide the name of this notebook session. If not, the system will automatically create one for you. Again, you can select Compute Shape as per your need and of which there are a lot of options.

So if you click on Change Shape, you can see you have a lot of options with respect to instance type shape series where you want to use AMD, Intel, or some other shape. And then you can also define the number of CPUs and amount of internal memory. And then click on Select Shape and that will select a compute shape for you. You can then define your block storage, networking resources, and endpoint type. And finally, then click on Create button here.

For this demo, I will click on this existing notebook session here, which now brings me to another page where you can see some additional information about the session itself, along with different metrics. I will open this active session and that will bring me to our Jupyter environment. Usually to begin with this notebook environment, you click on this new launcher. That will open a Launcher tab. These usually have environment kernels along with some other resources.

The first step is usually creating a Conda environment, which is a prepackaged environment with multiple libraries as per your use case. So let's click on Environment Explorer, which will open another tab for you. Here you can see multiple Conda environments. Let's expand any one of it. So here you can see some description about that particular Conda environment, what are the different libraries or packages in that environment, as well as the steps to install it. So let's copy this.

And to install it, you go back to Launcher. You click on the Terminal, which should open a terminal for you. And then you Copy-Paste the command and run it. So once you Copy-Paste and run it, it will install this Conda environment. And probably after refreshing this, you should see an additional kernel right here. Once you see your choice of kernel created here, click on Conda environment kernel. For example, I will click on this, and then click on Create Notebook, which will create a Jupyter Notebook for you.

So I have already created a Jupyter Notebook using this Conda environment. So my Conda environment is general ML, machine learning with Python version 3.8. And this is the Conda environment. You can also select or change your Conda environment kernel right from here. The code in this notebook is very similar to what we saw earlier in the machine learning module, with some additional libraries, such as ADS as needed and some extra steps to showcase data science service. So we will start with importing required libraries.

So let's complete this step. Then we will load the iris data set as we did earlier. So we have loaded the iris data set. Then again, we will split the data set into features and target variable. Split the data set further into training and testing sets. Let's see what each of the data frame shows. So this is the features. These are the features. And this is the target variable showing the first five rows of the data set.

Now again, let's train the model, train the classifier. In this case, we are going to use random forest classifier. Once you've trained the model using the framework of your choice, which we just did now, we will create a model object and call this prepare method, which generate all the required model artifacts needed to deploy a functioning model without you having to configure it or write any code. ADS library, which we had imported earlier, help with all of that.

So let's run this particular cell. Next, you can then call the summary_status method, which will return a pandas data frame that guides you through the entire workflow. So let's run this cell. This will show which methods are available to call and which ones aren't. Plus it also outlines what each method does. And then if extra actions are required, it also shows those actions. So you can see the output now. So all the steps, initiate, prepare, verify, save, deploy, and predict and their respective status, as well as any action needed, along with the details.

So you can see we have initiated and we have prepared. Those two steps are completed. So the verify method now, it simulates a model deployment. That means you can debug your files or test the model without actually deploying a model. So let's run .verify. So you can see from the test data set, for the first 10 rows it has done the prediction successfully. Then comes the Save method. The Save method deploys a model artifact to the model catalog. Let's run this cell.

So now the model is successfully loaded. Now you can see the first four steps, initiate, prepare, verify, and save, are completed. The deploy method. It deploys a model to a REST endpoint, and the predict method here, it generates prediction by invoking this deployed endpoint. So due to limited scope of this demo, we want to go further beyond saving a model.

But again, I have written the steps for you in case if you want to complete these further steps on your own. One other thing I want to show you is this model itself. So let's go back to our notebook sessions. If you click on the models, you will see this newly created sklearn model.

