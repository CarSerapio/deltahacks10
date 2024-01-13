# deltahacks10
DeltaHacks 10 submission

## Inspiration
TEMP VIDEO, RECORDING UPLOADED AT SUBMISSION *DELETE AFTER*
Language barriers have always a hindering factor to conversation quality, especially in businesses. When two businesses of different demographics are attempting to make something work, the general solution is to make the gold standard of business languages to be English. However, many successful businesses have found success in growth with the primary usage of other languages within the company such as [Japan's Honda](https://hbr.org/2012/05/global-business-speaks-english#:~:text=More%20and%20more%20multinational%20companies,across%20geographically%20diverse%20functions%20and). However, with English as the gold standard, companies are forced to adapt to this business system as there is not an easy way to directly communicate company to company with distinctive cultures. The heart of a business is the foundation and structure of their unique culture, and adaptation to compensate for language barriers can be an inconvenience or in worst-case, stray the company away from its roots. So instead of tens of millions of companies around the world constantly adapting to new standards, why not allow companies stick to their own cultures while still cultivating growth with other businesses with a simplistic communication software that allow people from all over the world to communicate in any language they are comfortable with. This is TalkBiz.

## What it does
TalkBiz is in summary a web conference platform like Zoom or Microsoft Teams with more complex ai-based features implemented to increase productivity with little adaptation needed for businesses. This software is designed to help businesses stay true to their own ways while having a powerful communication tool to talk business with others no matter what language they speak. Other than the typical elements you see in a web conferencing application, TalkBiz features 2 major elements.\\
The first feature is a voice cloning element where speaking into the mic in a certain language will output the same phrase translated into another language with the same voice. Yes, if you speak into the mic in english and you want to talk to your kpop idol over TalkBiz, they will hear you speak Korean fluently.\\
Our second feature is an automatic meeting minutes generator where after any long meeting, it takes speech from both sides of a conversation in a transcript format and summarizes key points from the convo into a meeting minutes document in respective languages. This allows more time and focus to get points across without the need of monitoring what the others say and instead alleviating the resource usage to be used for more businessy stuff.

## How we built it
To make the application features, surprise surprise, we used the power of machine learning and artificial intelligence. The first feature of translating speech from a language to another language requires multiple steps. The first being the training of a ML model from [Elevenlabs](https://elevenlabs.io) to first voice clone through inputs from a dataset consisting of many recordings of your own voice and translations using Google Translate's API. Once the model is trained enough, it stores your voice into your profile ready to be used for conversations. At this point, the AI can replicate your voice for all phrases in not only English, but in many other common languages as well. TalkBiz will have options to change the language you want to converse in and essentially speak in any language you would like.\\
Next for the second feature on meeting summerization, we will use [Microsoft Azure's text analytics library](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-textanalytics-readme?view=azure-python&viewFallbackFrom=azure-python-preview&preserve-view=true) AI tool for document summerization. In the backend, this takes the transcript from STT to a file and efficiently summarizes key points from the transcript to a friendly format meeting minutes document. On the front-end, this would appear as a condensed document of the meeting minutes notes.

## Challenges we ran into
While programming the project, we ran into a lot of compatibility issues and bug fixing which caused issues with the time management of the little time we had. With different frameworks requiring specific technology specs, it was hard to find the optimal version to work the project with all features together. Bringing all of the features to work in conjunction was also really difficult to implement without costs of performance as there is multiple APIs and libraries bundled into the project that are not optimized for one another.

## Accomplishments that we're proud of
A first accomplishment is that we have a compelling project to present with usages of many modern programming practices including a simplistic front-end design backed up by many features from the back-end with the utilization of AI modelling and content-dense APIs. Through the challenges we had, we put a lot of work into making bug fixes and adjustments to bring forth a working product that our current selves can make within 24 hours.

## What we learned
On the programming side, we learned from scratch how to tinker with the ElevenLabs speech to speech model for our AI voice cloning feature and combining it with a translation API for giving our voice the ability to speak like a talented polyglot. Using inspiration and demos of multiple Azure APIs and Cohere's API, we accomplished making a simple meeting summarization feature that consistantly produces a quality document with key interests from transcripts. Most importantly, from prior hackathon experiences, we learned how to work efficiently as a team putting our major strengths to appropriate tasks and knocking down our weaknesses by taking initiatives on tasks that require some overcoming of some uncomfortability.

## What's next for TalkBiz
Due to the 24 hour timeline, we could only create the application to work with a couple languages to start, but obviously there is not only 2 languages that people speak in today's world. For TalkBiz to become a solid application, all languages must be covered with precision, whether it would require more modernized translation APIs to be implemented or more complex training methodologies for the general AI model, this accuracy bump would make TalkBiz a refreshing start to virtual communication platforms.