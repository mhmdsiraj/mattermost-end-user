import os
import re
import json

base_path = r"c:\Users\××Owner\Desktop\Workspace Tasks\starlight\mattermost-end-user\src\content\docs"
structure_file = r"c:\Users\××Owner\Desktop\Workspace Tasks\starlight\mattermost-end-user\structure.text"
astro_config_file = r"c:\Users\××Owner\Desktop\Workspace Tasks\starlight\mattermost-end-user\astro.config.mjs"

translation_map = {
    "End User Guide": "دليل المستخدم النهائي",
    "Access Your Workspace": "الوصول إلى مساحة عملك",
    "Install the desktop app": "تثبيت تطبيق سطح المكتب",
    "Install the iOS mobile app": "تثبيت تطبيق iOS المحمول",
    "Install the Android mobile app": "تثبيت تطبيق Android المحمول",
    "Client availability": "توفر العميل",
    "Log out of Mattermost": "تسجيل الخروج من Mattermost",
    "Messaging Collaboration": "التعاون في المراسلة",
    "Organize using teams": "التنظيم باستخدام الفرق",
    "Team Settings": "إعدادات الفريق",
    "Team Keyboard Shortcuts": "اختصارات لوحة مفاتيح الفريق",
    "Organize using custom user groups": "التنظيم باستخدام مجموعات المستخدمين المخصصة",
    "Invite people": "دعوة الأشخاص",
    "Learn about Mattermost roles": "تعرف على أدوار Mattermost",
    "View system information": "عرض معلومات النظام",
    "Collaborate within channels": "التعاون داخل القنوات",
    "Channel types": "أنواع القنوات",
    "Channel naming conventions": "اصطلاحات تسمية القنوات",
    "Communicate a channel's focus and scope": "توصيل تركيز القناة ونطاقها",
    "Create channels": "إنشاء قنوات",
    "Rename channels": "إعادة تسمية القنوات",
    "Display channel banners": "عرض لافتات القناة",
    "Auto-translate messages": "الترجمة التلقائية للرسائل",
    "Convert public channels to private channels": "تحويل القنوات العامة إلى قنوات خاصة",
    "Convert group messages to private channels": "تحويل الرسائل الجماعية إلى قنوات خاصة",
    "Join and leave channels": "الانضمام إلى القنوات ومغادرتها",
    "Make calls in Mattermost": "إجراء مكالمات في Mattermost",
    "Manage channel members": "إدارة أعضاء القناة",
    "Browse channels": "تصفح القنوات",
    "Navigate between channels": "التنقل بين القنوات",
    "Mark channels as favorites": "تمييز القنوات كمفضلة",
    "Manage channel bookmarks": "إدارة الإشارات المرجعية للقنوات",
    "Mark channels as unread": "تمييز القنوات كغير مقروءة",
    "Archive and unarchive channels": "أرشفة القنوات وإلغاء أرشفتها",
    "Communicate with messages and threads": "التواصل باستخدام الرسائل والمواضيع",
    "Send messages": "إرسال الرسائل",
    "Reply to messages": "الرد على الرسائل",
    "React with emojis and GIFs": "التفاعل باستخدام الرموز التعبيرية وملفات GIF",
    "Organize conversations": "تنظيم المحادثات",
    "Forward messages": "إعادة توجيه الرسائل",
    "Share links to channels and messages": "مشاركة الروابط للقنوات والرسائل",
    "Save and pin messages": "حفظ الرسائل وتثبيتها",
    "Set message reminders": "تعيين تذكيرات الرسائل",
    "Search for messages": "البحث عن الرسائل",
    "Schedule messages": "جدولة الرسائل",
    "Flag messages": "تمييز الرسائل",
    "Format messages": "تنسيق الرسائل",
    "Set message priority": "تعيين أولوية الرسالة",
    "Mention people": "الإشارة للأشخاص",
    "Share files in messages": "مشاركة الملفات في الرسائل",
    "Collaborate within Microsoft Teams": "التعاون داخل Microsoft Teams",
    "Keyboard shortcuts": "اختصارات لوحة المفاتيح",
    "Keyboard Accessibility": "إمكانية الوصول للوحة المفاتيح",
    "Extend Mattermost with integrations": "توسيع Mattermost باستخدام عمليات الدمج",
    "Workflow Automation": "أتمتة سير العمل",
    "Learn about collaborative playbooks": "تعرف على كتيبات اللعب التعاونية",
    "Work with collaborative playbooks": "العمل مع كتيبات اللعب التعاونية",
    "Work with runs": "العمل مع عمليات التشغيل",
    "Work with tasks": "العمل مع المهام",
    "Work with notifications and updates": "العمل مع الإشعارات والتحديثات",
    "Work with metrics and goals": "العمل مع المقاييس والأهداف",
    "Share and collaborate": "المشاركة والتعاون",
    "Interact with collaborative playbooks": "التفاعل مع كتيبات اللعب التعاونية",
    "Audio and Screensharing": "مشاركة الصوت والشاشة",
    "Project and Task Management": "إدارة المشاريع والمهام",
    "Navigate boards": "التنقل في اللوحات",
    "Work with boards": "العمل مع اللوحات",
    "Work with cards": "العمل مع البطاقات",
    "Work with views": "العمل مع العروض",
    "Work with groups, filter, and sort": "العمل مع المجموعات والفرز والتصفية",
    "Work with calculations": "العمل مع الحسابات",
    "Import, export, and migrate": "الاستيراد والتصدير والترحيل",
    "Boards settings": "إعدادات اللوحات",
    "AI Agents": "وكلاء الذكاء الاصطناعي",
    "Agents usage tips and best practices": "نصائح استخدام الوكلاء وأفضل الممارسات",
    "Agents context management": "إدارة سياق الوكلاء",
    "Customize Your Preferences": "تخصيص تفضيلاتك",
    "Manage your notifications": "إدارة إشعاراتك",
    "Troubleshoot notifications": "استكشاف أخطاء الإشعارات وإصلاحها",
    "Manage your web notifications": "إدارة إشعارات الويب الخاصة بك",
    "Manage your desktop notifications": "إدارة إشعارات سطح المكتب الخاصة بك",
    "Manage your mobile notifications": "إدارة إشعارات هاتفك المحمول",
    "Manage your thread reply notifications": "إدارة إشعارات الرد على المواضيع",
    "Manage your @mention & keyword notifications": "إدارة إشعارات الإشارة @ والكلمات الرئيسية",
    "Manage your channel-specific notifications": "إدارة إشعاراتك الخاصة بالقنوات",
    "Customize your Mattermost theme": "تخصيص سمة Mattermost الخاصة بك",
    "Customize your channel sidebar": "تخصيص شريط القناة الجانبي",
    "Manage your profile": "إدارة ملفك الشخصي",
    "Manage your security preferences": "إدارة تفضيلات الأمان الخاصة بك",
    "Set your status & availability": "تعيين حالتك وتوافرك",
    "Manage your display options": "إدارة خيارات العرض الخاصة بك",
    "Manage your sidebar options": "إدارة خيارات الشريط الجانبي",
    "Manage advanced options": "إدارة الخيارات المتقدمة",
    "Manage your plugin preferences": "إدارة تفضيلات المكونات الإضافية",
    "Customize your desktop app experience": "تخصيص تجربة تطبيق سطح المكتب",
    "Connect to multiple workspaces": "الاتصال بمساحات عمل متعددة"
}

def kebab_case(s):
    s = s.replace('@', '')
    s = s.replace('&', '')
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    return '-'.join(s.lower().split())

with open(structure_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

sidebar = []
stack = [] # contains tuples of (level, list_of_items, current_kebab_path)

for line in lines:
    line_stripped = line.rstrip()
    if not line_stripped:
        continue
    
    match = re.match(r'^([\|\s-]*)(.*?)\s+\[(.*?)\]$', line_stripped)
    if not match:
        continue
        
    prefix = match.group(1)
    name_english = match.group(2).strip()
    node_type = match.group(3).strip()
    
    # Calculate depth
    level = prefix.count('|')
    
    arabic_name = translation_map.get(name_english, name_english)
    kebab_name = kebab_case(name_english)
    
    # adjust stack
    while stack and stack[-1][0] >= level:
        stack.pop()
        
    current_list = stack[-1][1] if stack else sidebar
    parent_path = stack[-1][2] if stack else ""
    
    if node_type in ("folder", "sub folder"):
        # We need to map it as a group in the sidebar
        new_group = {
            "label": arabic_name,
            "items": []
        }
        current_list.append(new_group)
        current_path = os.path.join(parent_path, kebab_name)
        stack.append((level, new_group["items"], current_path))
        
        # Create directory
        dir_path = os.path.join(base_path, current_path)
        os.makedirs(dir_path, exist_ok=True)
        
    elif node_type == "page":
        # It's a page, map as link
        slug = (parent_path + "/" + kebab_name).strip("/")
        slug = slug.replace("\\", "/") # ensure forward slashes
        new_link = {
            "label": arabic_name,
            "slug": slug
        }
        current_list.append(new_link)
        
        # Create md file
        dir_path = os.path.join(base_path, parent_path)
        os.makedirs(dir_path, exist_ok=True)
        md_file = os.path.join(dir_path, kebab_name + ".md")
        
        frontmatter = f"---\ntitle: \"{arabic_name}\"\n---\n"
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(frontmatter)

# Generate sidebar string
def stringify_sidebar(sb, indent=4):
    lines = []
    spaces = ' ' * indent
    lines.append('[\n')
    for item in sb:
        if 'items' in item:
            lines.append(spaces + '{')
            lines.append(spaces + f"    label: '{item['label']}',")
            lines.append(spaces + "    items: " + stringify_sidebar(item['items'], indent + 4).lstrip() + ",\n")
            lines.append(spaces + '},')
        else:
            lines.append(spaces + '{')
            lines.append(spaces + f"    label: '{item['label']}',")
            lines.append(spaces + f"    slug: '{item['slug']}',")
            lines.append(spaces + '},')
    lines.append('\n' + ' ' * (indent - 4) + ']')
    return ''.join(lines)

sidebar_str = stringify_sidebar(sidebar, 12)

# Update astro.config.mjs
with open(astro_config_file, "r", encoding="utf-8") as f:
    config_content = f.read()

# Replace the sidebar array using regex
import re
new_config = re.sub(
    r"sidebar:\s*\[.*?\](,\s*locales:)",
    f"sidebar: {sidebar_str}\\1",
    config_content,
    flags=re.DOTALL
)

with open(astro_config_file, "w", encoding="utf-8") as f:
    f.write(new_config)

print("sidebar injected into astro config successfully")
