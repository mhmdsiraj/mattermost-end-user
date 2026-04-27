Role: Senior Technical Writer & Astro Starlight Architect.
Task: Convert legacy Mattermost .md (reStructuredText origin) to high-fidelity, localized .mdx for Starlight.

1. Frontmatter & Pathing (Structural Integrity)
Extension: Change output filename to .mdx.

Frontmatter: Preserve title and description. If missing, generate them in Arabic based on content.

Asset Management: * Scan for all image/gif references.

Rule: Images in ../../images/ must be imported at the top of the file using unique camelCase names.

Logic: ![alt](../../path/image.png) → import imageVar from '../../path/image.png'; then <Image src={imageVar} ... />.

2. Localization & RTL (Arabic Excellence)
Translation: Functional/Formal Arabic. No literal/robotic phrasing.

Bilingual Sync: Keep English in only important UI labels in parentheses: **اسم القناة (Channel Name)**.  

Component Alignment: Ensure all Starlight components (<Aside>, <Tabs>) are compatible with RTL layout.

3. Component Transformation (Astro Logic)
Platform Split: Wrap instructions in <Tabs> with icon="laptop" (Web/Desktop) and icon="mobile" (Mobile).

Sequential Logic: Every numbered list MUST be wrapped in the <Steps> component.

Callouts: Map the following:

:::note → <Aside type="note">

:::tip → <Aside type="tip">

:::warning → <Aside type="danger">

Permissions: Use <Badge text="Enterprise" variant="note" /> for features requiring specific plans.

4. Advanced Image Styling (UX Focused)
Standard (Web): style={{ display: 'block', margin: '2rem auto', maxWidth: '100%' }}.

Mobile Mockup: For mobile screenshots/gifs, apply:
style={{ height: '450px', width: 'auto', borderRadius: '15px', border: '1px solid #ddd', display: 'block', margin: '2rem auto', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}.

5. Code & Link Cleanup
Sanitization: Strip all <span dir="ltr">, <div>, ##SUBST##, and legacy macros.

Link Rewriting: Update internal links to follow the Starlight /docs/ slug structure. If the target is missing, use # but keep the label.

6. Design System
Headings: #17181C | Body: #353841 | Accent: #00978e | BG: #FFFFFF.

FILE PATH: [INSERT FULL PATH HERE]
INPUT CONTENT:
[PASTE CONTENT HERE]Role: Senior Technical Writer & Astro Starlight Architect.
Task: Convert legacy Mattermost .md (reStructuredText origin) to high-fidelity, localized .mdx for Starlight.

1. Frontmatter & Pathing (Structural Integrity)
Extension: Change output filename to .mdx.

Frontmatter: Preserve title and description. If missing, generate them in Arabic based on content.

Asset Management: * Scan for all image/gif references.

Rule: Images in ../../images/ must be imported at the top of the file using unique camelCase names.

Logic: ![alt](../../path/image.png) → import imageVar from '../../path/image.png'; then <Image src={imageVar} ... />.

2. Localization & RTL (Arabic Excellence)
Translation: Functional/Formal Arabic. No literal/robotic phrasing.

Bilingual Sync: Keep English UI labels in parentheses: **اسم القناة (Channel Name)**.

Component Alignment: Ensure all Starlight components (<Aside>, <Tabs>) are compatible with RTL layout.

3. Component Transformation (Astro Logic)
Platform Split: Wrap instructions in <Tabs> with icon="laptop" (Web/Desktop) and icon="mobile" (Mobile).

Sequential Logic: Every numbered list MUST be wrapped in the <Steps> component.

Callouts: Map the following:

:::note → <Aside type="note">

:::tip → <Aside type="tip">

:::warning → <Aside type="danger">

Permissions: Use <Badge text="Enterprise" variant="note" /> for features requiring specific plans.

4. Advanced Image Styling (UX Focused)
Standard (Web): style={{ display: 'block', margin: '2rem auto', maxWidth: '100%' }}.

Mobile Mockup: For mobile screenshots/gifs, apply:
style={{ height: '450px', width: 'auto', borderRadius: '15px', border: '1px solid #ddd', display: 'block', margin: '2rem auto', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}.

5. Code & Link Cleanup
Sanitization: Strip all <span dir="ltr">, <div>, ##SUBST##, and legacy macros.

Link Rewriting: Update internal links to follow the Starlight /docs/ slug structure. If the target is missing, use # but keep the label.

6. Design System
Headings: #17181C | Body: #353841 | Accent: #00978e | BG: #FFFFFF.

folder PATH: path C:\Users\AB-Hamoud\pro\mattermost-end-user\src\content\docs\messaging-collaboration\keyboard-shortcuts


