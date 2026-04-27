we have mattermost project our tasks is to develop docs for it.
we use starlghit astro for it.
the goal is to develope docs for it. 
all docs of mattermost was build have e.rst format we convert it to md files and then we use astro to build the docs. 
I have 1 problem with it.
Role: You are a Senior Technical Writer and Astro Starlight Developer specializing in professional enterprise documentation.
Task: Transform the provided Markdown/MDX content into a modern, highly polished, and professional Starlight MDX page 

path : C:\Users\AB-Hamoud\pro\mattermost-end-user\src\content\docs\workflow-automation\*.md

Core Instructions:

Component Integration: Replace standard Markdown with Starlight components:
Use <Tabs> and <TabItem> to separate "Web/Desktop" from "Mobile" instructions.
Use <Steps> for all ordered instruction lists.
Use <Aside> for notes (note), tips (tip), and warnings (danger).
Use <Badge> to indicate version or plan availability (e.g., Enterprise).
All images  in content should be in the same path in the docs.
we will copy the content of .md file and create new one with .mdx extension and put content of .md in it ,and start apply mdx on it .
apply and process full content of files not part of it.
any files with  .mdx extention was note processed as required or it is not  containing full content of the .md file you have to fix that.

we will start processing  the path we mentioned it previously 
without deleting the original docs or files with .md extensions.
take care of design and style and avoid syntax errors 
you can use any components of astro and import any thing you use from it like {Image,Tabs,TabItem,Badge,etc...}.
Image Styling (Critical):
Convert standard ![]() images for example :
import { Image } from 'astro:assets';
import myImage from "../../../../images/mobile-edit-a-channel-bookmark.gif";
  <Image src={myImage} alt="حذف الإشارة" height="500" />
  ## ⚙️ إدارة الإشارات المرجعية

Constraint: For mobile screenshots, apply a fixed height (e.g., 450px), width: auto, and a borderRadius: '15px' to mimic a real phone screen.
Ensure images are centered using display: 'block' and margin: 'auto'.
Code Cleanup: Remove all legacy HTML noise (<span dir="ltr">, <div>, ##SUBST##, broken macros).
Information Architecture: Use clear headings, bullet points, and tables for comparison.
Example of Input Style to Fix:
![Plan Icon](##SUBST##) Available on Enterprise [link]
<div class="tab">Mobile Step 1...</div>
Example of Expected Output Style:
<Aside type="note"><Badge text="Enterprise" /> متاح في نسخة...</Aside>
<Tabs><TabItem label="الهاتف">...</TabItem></Tabs>
Content to transform: start apply from C:\Users\AB-Hamoud\pro\mattermost-end-user\src\content\docs\*\*\*.md or *.mdx
change the extension of the name of file *.mdx instead of *.md
you can skip if the directory is empty
How the AI will apply this (Examples)
Example 1: Fixing "Plan Availability"
Old MD: <Aside type="note">[|plans-img-yellow|] Available on Entry, Professional, Enterprise</Aside>
New MDX (AI Output):
code
Mdx
<Aside type="note" title="توفر الميزة">
  متوفر في خطط: <Badge text="Entry" variant="note" /> <Badge text="Professional" variant="note" /> <Badge text="Enterprise" variant="note" />
</Aside>
Example 2: Fixing Mobile Screenshots (Phone Height)
Old MD: ![Mobile Screen](../../image.jpg)
New MDX (AI Output):
code
Mdx
<img 
  src="../../image.jpg" 
  alt="واجهة الهاتف" 
  style={{ height: '450px', width: 'auto', borderRadius: '15px', border: '1px solid #ddd', display: 'block', margin: '10px auto' }} 
/>
Example 3: Platform Separation
Old MD: A long page with "Web instructions" then "Mobile instructions" below it.
New MDX (AI Output):
code
Mdx
<Tabs>
  <TabItem label="سطح المكتب" icon="laptop">
    <Steps>
      1. افتح المتصفح...
      2. أدخل الرابط...
    </Steps>
  </TabItem>
  <TabItem label="الهاتف المحمول" icon="mobile">
    <Steps>
      1. حمل التطبيق...
      2. سجل الدخول...
    </Steps>
  </TabItem>
</Tabs>
do not remove urls links or any texts noises just take care of design and transforming do not ignore or remove any information. 
last point is to fix url links that used in content of .mdx files based on the local structure. 
2- for translation to arabic:
   our audiance is arabic people so we must translate all the docs to arabic but in english not literal translation but in functional and formal way as possible.
   
*** construction ***
we will use the next rules to build the docs:
- we will take care of the design and styles of each page.
- we will  use .mdx instead of .md format for batter experience.
- we already have the structure and the content in the original docs.
- we will apply the rules in the original docs.
- we will use Primary color: #00978e,Headings color: #17181C,Text color: #353841,Background Color: #fff


- we will use the same rules to format the new docs.
- we will copy the content of .md file and create new one with .mdx extension and put content of .md in it ,and start apply mdx on it 
- we will check links of the page content if url exists in local configuration folders/files put urls in its place else leave it empty
- we will start processing  file by file starting the path we mentioned it previously 
-
- all images in content should be in the same path in the docs.
- Transform the provided Markdown/MDX content into a modern, highly polished, and professional Starlight MDX page 


Role: Senior Technical Writer & Astro Starlight Developer.
Task: Transform legacy Mattermost .md content into a high-performance, RTL-ready .mdx page.

1. Structure & Components
Platform Tabs: ALWAYS separate "Web/Desktop" and "Mobile" using <Tabs> and <TabItem>. Use icon="laptop" and icon="mobile".

Procedures: Wrap every numbered list in the <Steps> component.

Callouts: Convert all :::note, > [!NOTE], or blockquotes into <Aside type="note | tip | caution | danger">.

Badges: Use <Badge text="Enterprise" variant="note" /> for plan-specific features.

2. Localization (Arabic RTL)
Tone: Professional, formal, and functional Modern Standard Arabic.

UI Preservation: Translate instructions but keep some of so important UI elements bilingual.

Example: "Click Settings" → "انقر على الإعدادات (Settings)".

Punctuation: Ensure punctuation follows Arabic grammar (Right-to-Left).

3. Image & Media Handling (Strict)
Imports: Create unique import names for every image at the top of the file.

Example: import renameMobile from '../../images/rename.png';

Standard Styles: <Image src={imgName} alt="..." style={{ display: 'block', margin: '2rem auto' }} />

Mobile Mockup Style: If the image is a mobile screenshot, apply:
style={{ height: '450px', width: 'auto', borderRadius: '15px', border: '1px solid #ddd', display: 'block', margin: 'auto' }}

4. Data Hygiene
Clean-up: Delete all <span dir="ltr">, <div> tags, ##SUBST## macros, and .rst leftover artifacts.

Link Mapping: Check all [links]. If the target exists in the local directory, update the path. If it refers to an external Mattermost doc, let path empty.

5. Design Specifications
Primary Accent: #00978e

Headings: #17181C

Body: #353841

Background: #FFFFFF

