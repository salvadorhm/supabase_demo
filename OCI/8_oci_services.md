# 1. OCI Language

OCI language is a fully managed, serverless natural language processing service. It lets you analyze unstructured text at scale using pre-trained models, or train your own custom models, all without needing any data science or machine learning expertise. In this lesson, we'll cover five pre-trained capabilities, then custom models, real-time translation, and finally two specialized capabilities-- PII and PHI detection and health NLP for clinical text.

OCI language analyzes unstructured text for you using models trained on industry data. So you get language analysis with no data science expertise needed. Think of it as ready-to-use AI that understands text the moment you send it to the service. It has five main pre-trained capabilities, and we'll go through each one using an example screen like this.

The first capability is language detection. Notice the greetings on this slide-- hello in English, konnichiwa in Japanese, hola in Spanish, and bonjour in French. OCI Language automatically detects which of more than 75 supported languages, from Afrikaans to Welsh, a piece of text is written in and returns a confidence score along with the detected language.

This slide continues the same five-capability overview, now demonstrating the second one-- Named Entity Recognition, or NER. NER scans text and picks out named entities, real-world objects that have a name, such as people, organizations, locations, dates, currency amounts, email addresses, and phone numbers. In the example on this slide, the service has picked out 3.3.22 as a date, along with a currency value and a name from the source text, each returned with its position in the text and a confidence score. This is useful anytime you need structure from freeform text, for example, tagging news articles by the people and places mentioned, routing customer support feedback, speeding up search by matching queries against extracted entities instead of full documents, or screening job candidate résumés by location, employer, and skills.

The third capability is sentiment analysis, and this slide shows why analyzing sentiment per aspect matters more than one overall score. Look at the review shown here-- "The food was great, but the service sucked." If we scored the whole sentence as one overall sentiment, the negative comment about service could cancel out or drag down the positive comment about food, and we'd lose useful detail.

OCI Language solves this with aspect-based sentiment analysis. It treats each aspect, here food and service, as an attribute of the review and scores each one independently. So we get food as positive and service negative, both from the same sentence, each with its own confidence score. The service also supports sentence-level sentiment so you can choose whichever granularity, document, sentence, or aspect that fits your use case, such as brand monitoring, product surveys, employee feedback, or customer review analysis.

The fourth capability is keyphrase extraction. It automatically pulls out the words and expressions that carry the most meaning in a block of text, rather than returning every word. It's a fast way to summarize a document or surface its main subjects without reading the whole thing. In the example on this slide from a passage about Java, the service extracts phrases like "Java Development Kit" and "Java 18." As the key phrases that represent the important subjects of the text, this is useful for quickly tagging or summarizing large amounts of content.

The fifth and final pre-trained capability is text classification. It assigns the text an overall topic from a predefined taxonomy of about 600 categories and subcategories, returned as a domain and subdomain, each with a confidence score. In this example, a short piece of text about a kitten, Kitten Digest Meow, is classified under the domain animals and plants and the subdomain pets.

The same mechanism can classify financial documents into categories like banking or investing, or sort news articles by topic. This slide summarizes the three ways you can use OCI Language-- pre-trained models, custom models, and text translation. Pre-trained models are the ones we just covered. Language detection, sentiment analysis, and keyphrase extraction are ready to use out of the box with no training required.

Custom models let you train the service on your own labeled data for two tasks-- named entity recognition and text classification. This is what you use when the built-in categories or entity types don't match your business. For example, your own support ticket categories or industry-specific terms. Text translation uses neural machine translation to translate text in real time between many supported languages, useful for multilingual support tickets, chatbots, or content moderation. And we'll look at it in a bit more detail shortly.

This slide walks through a concrete example of why you would build a custom model. Imagine a support team that receives thousands of tickets every day, and each ticket needs to be routed to the right department. Historically, a person read each ticket and decided where to send it. This is slow, repetitive, and hard to scale.

With OCI Language, you create a custom text classification model and train it on examples of tickets that humans have already routed in the past. The model learns the patterns behind each routing decision. For example, which words and phrases tend to point to which department?

Building a custom model generally follows five steps. Prepare a labeled training data set. Train the model. Evaluate it using metrics like precision, recall, and F1 score. Deploy it to an endpoint once you are happy with the metrics. And then use that endpoint to analyze new text. Once trained and deployed, the model can automatically classify new incoming tickets and route them to the correct department.

PII and PHI detection is a specialized capability for protecting private information in text. PII stands for Personally Identifiable Information-- things like names, addresses, phone numbers, or ID numbers. PHI stands for Protected Health Information, the healthcare-specific version of the same idea.

The service detects these sensitive entities in unstructured text, classifies what type of private information each one is, and then gives you options to de-identify it. You can mask it, replace it with a placeholder, or remove it entirely before the text is stored or shared further. Common use cases include automatically warning users when they're about to submit personal data in a feedback form and scanning large volumes of documents in Object Storage to make sure sensitive information isn't sitting somewhere it shouldn't be.

Health NLP is a set of models purpose-built for clinical and health care text, such as electronic health records, physician progress notes, and clinical trial documents. It's really a set of models working together. Health-Named Entity Recognition, or Health NER, finds clinical entities in text-- things like medical conditions, medications, dosages, symptoms, test results, treatments, and procedures. Medical entity linking then connects those extracted entities to standard medical coding systems-- SNOMED-CT and ICD-10.

So free text becomes structured, coded data that other health care systems can use. Relationship extraction goes a step further, identifying how different medical entities relate to each other in the text. For example, linking a medication to its correct dosage or duration. Together, these models help automate tasks, like clinical documentation review, medical coding, and clinical decision support.

# 2. Demo: Language

Let's look at OCI Language in the console. Now, this is the console home screen. Yours might look the same or different, just depending on a number of factors. But what you need to do is go to the menu Analytics & AI. Under AI Services, we have Language.

And we're going to go in here, and now we see the Language page. And there's some good resources here that you might be able to take advantage of. One, if you're interested in particular topics, you can use the links here to take you right into the documentation. Also some resources listed over here, like the API reference, SDK guide and such other listing of blogs related to OCI Language service.

But what we want to do right now is just actually try out the service. So let's go into Text Analytics. And you can see there's some default text already in here that we can analyze, and all you have to do is analyze it. Just click the Analyze button.

And we see the different kinds of analysis that the language service produces. So first we see the language detection, which is English, and the confidence indicator here-- very high. The classification of the text is listed as science and technology, with a subcategory of Earth sciences, and a fairly low probability on that one.

But you can see it's actually accurate in this case. We see the text with the named entities highlighted. So it highlights both the entity, the type of entity, and then the confidence. And so we see different color codings for different types of entities, from locations, quantities, products, date times.

And then the next area is the key phrase extraction. So in this case, it's just listing all of the key phrases that were extracted from the text. And then for sentiment, we get three different types of sentiment. So we get a document-level sentiment, which refers to the whole text and indicates as mixed, and then we get the aspect-based sentiment, which are specific aspects that it is identified in the text, which then it assigns a sentiment to those. And in all cases, these were negative sentiments.

And then it also provides a sentence-level sentiment. So for each sentence in the provided text, it assigns either a positive, neutral, or negative sentiment. And you can see we've got some of each in this example. So now you get an idea of what OCI Language provides in terms of the analysis.

# 3. OCI Speech

OCI Speech uses Automatic Speech Recognition, or ASR, to turn audio and video files into accurate, readable text, with no data science background required. In this lesson, we'll look at how OCI Speech works, transcription jobs using both the Oracle and Whisper models, and live real-time transcription and features like normalization and profanity filtering.

OCI Speech is very straightforward. It unlocks the data in audio tracks by converting speech to text. Developers can use Oracle's time-tested acoustic and language models to provide highly accurate, grammatically correct transcription for audio or video files across multiple languages. In this slide, you can see the basic flow.

An input audio signal-- here, a clip from an Oracle earnings call-- goes in on the left, and clean, readable output text comes out on the right, already punctuated and formatted like something a person would write. Under the hood, this uses Automatic Speech Recognition, or ASR, a type of AI model trained to map sound waves to written words. Unlike a simple dictation app, OCI Speech is built to handle real-world, imperfect audio-- conference calls, customer service recordings, and meetings with background noise and multiple speakers.

OCI Speech automatically transcribes audio and video files into text using advanced deep learning techniques. No data science expertise is required. You call a managed API and get text back without training or tuning any models yourself. Processes data directly in object storage. You point the service at audio or video files already sitting in a bucket, and it writes the transcription results back to a bucket you choose, with no need to move files anywhere else first.

Generates timestamped, grammatically accurate transcriptions. Every word gets a timestamp, so you can jump straight to the moment in the recording where something was said, which is great for searching long recordings. A transcription job is simply an asynchronous request. You submit one or more media files, and the service processes them in the background and writes results to object storage when done.

Each job can contain up to 100 individual files called tasks, and jobs are retained for 90 days, so you can go back and retrieve results. OCI Speech actually gives you a choice of two transcription models for creating a job-- the Oracle ASR model and the Whisper model. We'll take a look at Oracle model, which is Oracle's own acoustic and language model built specifically for OCI Speech, and then the Whisper model, which is OpenAI's multilingual model made available through the same service.

Whisper is a model originally built by OpenAI. It was trained on a huge amount of multilingual audio collected from the web, so it supports more than 50 languages, far more than the Oracle ASR models' seven or so languages, which makes it a good choice when you need broad language coverage. Like the Oracle model, Whisper also supports diarization, the process of labeling which parts of a recording were said by which speaker.

This is done in two steps. Speaker segmentation, which finds the points where the speaker changes; and speaker clustering, which groups segments together by who's talking. Importantly, Whisper uses the exact same service endpoints and API and SDK interfaces as the Oracle ASR model. In practice, that means switching between the two models is just a configuration choice when you create a transcription job. Your integration code doesn't need to change.

So far, we've talked about transcription jobs, which are asynchronous. You submit a file and get results back later. Live Transcribe is different. It provides real-time transcription, so you send a live audio stream to the service and get text results back within a couple of seconds. This matters for use cases where you can't wait for a batch job to finish. Think of a call center that wants to display live captions to an agent while a customer is talking, or a media company adding live captions to a broadcast. A great example from health care. Physicians and nurses use medical dictation while examining a patient, and they read the transcription to appear as they speak, not minutes later, so it fits naturally into their workflow. Behind the scenes, you can configure things like which model and language to use and how punctuation is applied.

This slide rounds up several more OCI Speech features. The Oracle ASR model supports English, Spanish, French, German, Portuguese, Hindi, and Italian. And remember, if you need broader language coverage, the Whisper model adds 50 plus more languages on top of that. It has batching support. So instead of submitting one call per audio file, you can submit multiple files together in a single job up to 100 files or tasks per job, which is much more efficient when you have a backlog of recordings to process. It also has blazing-fast processing. It can transcribe 10 hours of audio in under 10 minutes.

It achieves this by chunking your audio into small segments, transcribing each segment in parallel, then joining the text back into a single file. It provides a confidence score per word and per transcription, so you can quickly spot the words the model was less certain about and decide whether they need a human to double-check them. It punctuates transcriptions automatically, adding commas, periods, and question marks to make text more readable and to let downstream systems process the text with less friction. And it has SRT file support. SRT is the most popular closed caption file format. With SRT output, you can add closed captions to your videos directly without a separate captioning tool. This slide covers two more features that make transcribed text more readable and appropriate.

The first is text normalization. It reshapes spoken numbers, currency, dates, and addresses into the form a person would actually write. For example, saying $1,355 out loud gets normalized in the transcript to $1,355, exactly as shown in the example here. The second feature is profanity filtering, and the example in this slide shows the same offensive word handled three different ways.

"Remove" replaces the word entirely with asterisks, so no trace of it remains. "Mask" does something similar, but keeps the first letter, giving you a hint of the word without spelling it out. And "tag" leaves the original word in the text, but flags it as profanity in the results, which is useful if a human reviewer still needs to see exactly what was said. That wraps up the core capabilities of OCI Speech. Together, these make speech a practical building block for call center analytics, subtitling, and searchable media archives.

# 4. Demo: Speech

Let's take a look at OCI Speech in the console. We'll use the menu to go to Analytics and AI, then under AI Services, we'll select Speech, and that takes us to the console page for Speech service.

Now, before we jump into using the service, one of the requirements is that we have some data already loaded into object storage, and we're going to have to create a transcription job to then convert the speech to text. Now, I'm selected a particular compartment here, where I know I have data already available.

So we'll start, and we'll create our transcription job. Let's call our job Training. I've already got the compartment is preselected.

I want to pick the right bucket here, the object storage bucket in my compartment where I know I have the data. And now, it shows me the data I have that's in that bucket, and I see a WAV file here. That's the one that I previously loaded, and we'll run the job.

Now, the job only takes a few seconds to run. I know, in this case, because I've run it several times before, and it's still in progress. Now, the job succeeded, and we can go down, select the file, and we see the transcription result.

So it says, I'm having an issue with my wireless headphones. I think my Bluetooth connectivity to the TV is not working. I have high quality headphones. I know the issue is not with them.

And then we see a second voice come in here. Hi, thanks for contacting support. I'm sorry to hear about your Bluetooth issue.

Now, notice the punctuation that has been added to here. We also see some normalization where, instead of spelling out the words 100 and percent, it's showing them symbolically. So we get a very nice transcription.

# 5. OCI Vision

OCI Vision is a serverless computer vision service. You upload an image and it tells you what's in it-- objects, scenes, text, and faces-- all without needing any data science expertise. In this lesson, we'll look at Vision's main capability, image analysis, and walk through the specific pre-trained features covering custom models.

Vision is a computer vision service that works on images. Think of it as giving your applications the ability to see a picture and describe what's in it, the same way a person would glance at a photo and immediately recognize objects, text, and faces. It provides two main capabilities, image analysis, which examines photographic images for objects, scenes, text, and faces; and stored and real-time video analysis with key features like object detections, face detection, and object tracking.

Image analysis looks at photographic images. Image classification labels the overall scene. It identifies the major features and objects present without necessarily drawing boxes around each one. In the example on this slide, a photo of a railway crossing is classified with labels like train, line, tree, cables, track, wires, and poles. A broad description of what the scene contains.

Object detection goes a step further. Instead of just labeling the whole scene, it finds each individual object inside the image, draws a bounding box around it, and gives each one its own confidence score. In the car example shown here, the service separately identifies the auto design, the car itself, the bumper, and the wheel, each with a confidence score above 98%.

This slide covers two more image analysis features-- text detection and face detection. Text detection, also called Optical Character Recognition, or OCR, finds and digitizes printed or handwritten text inside an image. It draws a bounding box around each piece of text it finds and returns a confidence score. Face detection finds human faces in an image and returns for each face its location, key facial landmarks, such as the eyes, nose, and mouth, and a visual quality score.

In the example in this slide, five different faces are each detected with their own confidence score, from face 1 at 94.59% down to face 5 at 89.83% Face detection has some practical uses worth calling out. You can use the face location to blur faces for privacy. Use the quality score to decide if a face is clear enough for downstream biometric checks, or tag photos with facial information for easier searching in a media library.

Image analysis pre-trained models are the ones we just walked through-- object detection, image classification, text detection, and face detection. They work immediately out of the box on general-purpose images. Image analysis custom models let you go further when the pre-trained categories don't fit your business. For example, custom object detection lets you train the service to find the location of your own custom objects in an image and provide a bounding box for them.

For example, detecting a specific piece of manufacturing equipment or a company logo. To build a custom model, you create a labeled data set of example images, instruct Vision to train a model on that data set, and then call the trained custom model to evaluate new images. The same train evaluate deploy pattern we saw earlier for custom models in OCI language.

# 6. Demo: Vision

Let's take a look at OCI Vision in the console. Here we are at the console homepage, and we'll navigate to Analytics and AI and to Vision. Now on the Vision homepage, you can see there's a number of resources here that are available to you. And then you can exercise the different features of the service, both the image analysis through image classification or object detection or the Document AI.

There's also a section there for creating custom models. We're not going to do that today. Let's just go right into image classification. Now the service already has some default images in here, that it will analyze. And you can quickly see what kind of tags it assigns for image classification purposes to this particular image-- overhead power line, transmission tower, plant, sky, line.

OK, that looks like pretty good results here. Let's bring in another image. I'm going to drag one in from my desktop here. Now this is an image of iconic London. You can see some famous landmarks here. What we get tagged in this image-- skyscraper, water, building, bridge, boat. All good tags for this kind of a scene.

All right, let's go into object detection. Same thing applies here. There's some default images that it will do object detection on immediately. So in this scene, now it's looking for specific objects in the scene. It puts a bounding box around those and then tags those.

And this is the same results you get in the actual data that comes back. And over here we see what those results are. But front center, we've got a car, all right? In the back, we've got a bus. Over here on the sidewalk, we've got some people. Over here is another car.

And even just a little fraction of a car is visible, but it still detects it. All right, those are the objects that were detected, but there's also some text in this scene that is detected. And that's highlighted now. It reads this license plate, reads the Oracle logo on this car.

It gets the bus route that's shown on there. I can't even read that in the image, but the object detection does. Also, it picks up the advertisement on this cab. Even way back there, it's picking up a route on that bus. So lots of information extracted from this image.

Now, let's take a look at another scene. Here's a small image, fairly low resolution. And you might not even notice it initially, but there's a person standing on this roof, which is a little unusual, but it picks out that person. It does not, however, do any object detection around these unusual circular objects, which happen to be microwave transmission antennas for communications purposes.

And the model is not trained to detect those. You could then build a custom model to detect those, if you'd like. But it's the person that it picks out in this particular image. Let's look at one more. Now here's a scene of some cyclists out on the road.

And this one's interesting because it detects the person, even though the person is hunched over end facing away from us. And it also detects that they're on a bicycle. And you can tell that because the boxes are nested, .

And then it even picks up a bicycle wheel associated with a bicycle. And same over here, a little further away, still detects a person and this person being on a bicycle. No text in this scene for it to recognize other than what it thinks is a dash on the person's clothing.

# 7. OCI Document Undertanding

Document understanding is a serverless AI service that reads documents like invoices, receipts, forms, and IDs and turns them into structured data you can act on with no prior data science expertise. In this lesson, we'll cover its four pre-trained capabilities, text extraction, table extraction, key value extraction, and document classification.

Document understanding is used for working with document images and files rather than general photographs. It reads business documents and turns them into structured data. You can use it to understand PDFs, document images like JPEG, PNG, and tiff, whether uploaded from a local file or straight from OCI Object Storage.

This slide introduces its four pre-trained capabilities. We'll go into each one in detail over the next few slides. Text extraction, powered by optical character recognition or OCR, pulls the actual words off the page, including handwritten text and text that's tilted, shaded, or rotated.

Document classification sorts documents into different types based on their visual appearance, high level features, and extracted keywords, for example, recognizing that a file is an invoice, a receipt, or a resume so you can route it correctly. Table extraction identifies tables inside a document and extracts their content in tabular form, keeping the row and column relationships intact. Very useful for invoices, purchase orders, and receipts.

Key value extraction finds the values for a predefined set of common fields and line items on documents like receipts and invoices, for example, the merchant's name and the transaction date without you having to tell it where to look.

This slide zooms in on the first pre-trained capability, text extraction. Text extraction uses optical character recognition, or OCR, to detect and recognize text in a document and it returns two levels of detail, word level text with a bounding box around each individual word and line level text with a bounding box around each full line.

Because you get bounding box coordinates alongside the text, you know exactly where on the page each word or line was found, not just what it says. That's what makes this useful for things like highlighting matched terms in a scanned contract or rebuilding a searchable version of a paper document.

Text extraction is the foundation the other three capabilities build on. Table extraction, key value extraction, and document classification all rely on first recognizing the text on the page before they can make sense of its structure or meaning. This slide covers the second pre-trained capability, table extraction. A lot of business documents, invoices, purchase orders, receipts, bank statements contain data laid out in tables, and simple text extraction alone would just give you a jumbled list of words with no sense of which cell each word belongs to.

Table extraction solves this by identifying the tables in a document, along with the individual cells inside them, and extracting the content while preserving the row and column relationships. So instead of a flat list of words, you get back structured tabular data you can load straight into a spreadsheet or a database. A common use case is invoice automation, extracting the line item's product, quantity, unit price from an invoice table so they can be processed automatically instead of a person retyping them by hand.

This slide covers the third pre-trained capability, key value extraction. Key value extraction goes beyond plain text and tables. It understands the meaning behind specific fields on a document. It identifies a predefined set of key fields on document types such as receipts, invoices, driver licenses, health insurance IDs, and passports.

For an invoice, for example, it doesn't just give you all the text on the page. It tells you specifically which piece of text is the vendor's address, which is the invoice date, and so on, along with a confidence score for each field it finds. This slide covers the fourth and final pre-trained capability, document classification.

Document classification looks at a document's visual appearance and high level features, not just the text on it, and assigns it to a document type. This slide lists its eight example types like invoice, receipt, bank statement, health insurance ID, driver license, passport, tax form, and resume.

This is usually the very first step in a document processing pipeline. Before you can decide whether to run key value extraction for an invoice or a driver's license, you first need to which one you're looking at. Document classification answers that question automatically.

# 8. Demo: Document Understanding

All right, let's go to Document AI. Now, the default image here is a receipt, and it detects it as English. And it extracts a lot of raw text off of this receipt. You can see everything that's highlighted here, which is the entire contents of the receipt, have been extracted. And we see what it is extracted here, both in line format or in individual word format.

Now, let's look and see if it got any key values, and yes, it did. Remember, that for receipts, it has a number of specific keys that it looks for, and then if it finds a matching value, it will assign that value to the key.

So we get the merchant name, example cafe, the merchant address, merchant phone number, transaction time, transaction date, a lot of information on this receipt that's useful in processing it as an expense. And then we also see the line item data down here, and we can also see tabular data. It's picked out both two items here, an Americano and a water.

Let's look at a different image example for Document AI. This is an invoice, and now, we see all the highlighted items of text that it has extracted, which is everything that's on the image. One thing that's interesting about this invoice, it's had a stamp put on it after it was received, which the accounts payable clerk used to process that invoice.

And we do extract some information off there, even though some of that is handwritten, and some of it's stamped. And the stamp is not very-- at least didn't come through very readable in the scan of that image. We see all the relevant information extracted.

Because this is an invoice, we're not doing key value extraction on it at this time, but we do pull some tabular data out here. So not only the quantities and descriptions and unit price in total, it also pulled, actually, some of the stamp information off and put it into the description column. But it didn't interfere with the other information that was extracted.

