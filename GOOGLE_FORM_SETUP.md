# Google Form Setup for Contact Button

## Step 1: Create the Google Form

1. Go to [Google Forms](https://forms.google.com)
2. Click **+ Blank** to create a new form
3. Title it: **Chaues Productions - Contact Form**
4. Add a description: "Get in touch for planning, guide services, or videography inquiries"

## Step 2: Add Form Sections with Conditional Branching

Google Forms will use **sections** to route people to the right options. Here's the structure:

---

### **SECTION 1: Contact Information**

#### Field 1: Name
- **Type**: Short answer
- **Question**: "Your Name"
- **Required**: Yes

#### Field 2: Email
- **Type**: Short answer
- **Question**: "Your Email Address"
- **Required**: Yes
- **Validation**: Click the three dots → Response validation → Text → Email address

#### Field 3: Location
- **Type**: Multiple choice
- **Question**: "Where are you located?"
- **Description**: "This helps me route you to the right options"
- **Options**:
  - **Japan** → Go to Section 2 (Japan options)
  - **Nashville, TN** → Go to Section 3 (Nashville options)
  - **Other** → Go to Section 4 (Other locations)
- **Required**: Yes
- **Action**: Click the three dots → Go to section based on answer

---

### **SECTION 2: Japan-Based Inquiries**

**Section Description**: *Are you a company/organization in Japan interested in partnering with Tokyo in Film? Select "Partnership" below. Looking to hire me for on-site work in Tokyo? I'm available in May 2026, or if you can cover travel expenses for other dates.*

#### Field 4: Inquiry Type (Japan)
- **Type**: Multiple choice
- **Question**: "What are you interested in?"
- **Options**:
  - **Partnership with Tokyo in Film course** → Go to Section 5 (Partnership)
  - **Hiring for May 2026 project in Tokyo** → Go to Section 6 (Tokyo May hiring)
  - **Hiring with travel coverage** → Go to Section 7 (Travel-covered hiring)
  - **Something else** → Go to Section 8 (Custom request)
- **Required**: Yes
- **Action**: Click the three dots → Go to section based on answer

---

### **SECTION 3: Nashville-Based Inquiries**

**Section Description**: *I'm based in Nashville and available for local projects year-round.*

#### Field 5: Service Packages (Nashville)
- **Type**: Multiple choice
- **Question**: "What type of project do you need?"
- **Options**:
  - **Videography Package** (shoot only) → Go to Section 9 (Service details)
  - **Full Production** (shoot + edit + direction) → Go to Section 9
  - **Editing Only** (you provide footage) → Go to Section 9
  - **Writing/Copyediting** (scripts, content) → Go to Section 9
  - **Consultation/Planning** (pre-production, location scouting) → Go to Section 9
  - **Custom Package** → Go to Section 8 (Custom request)
- **Required**: Yes
- **Action**: For standard packages → Go to Section 9; For custom → Go to Section 8

---

### **SECTION 4: Other Locations**

**Section Description**: *For projects outside Nashville or Japan, I'm available remotely (editing, writing) or on-site if travel is covered.*

#### Field 6: Remote or On-Site?
- **Type**: Multiple choice
- **Question**: "What type of work do you need?"
- **Options**:
  - **Remote work** (editing, writing, consultation) → Go to Section 10 (Remote work)
  - **On-site work** (I travel to your location, you cover expenses) → Go to Section 11 (Travel work)
  - **Not sure / Custom request** → Go to Section 8 (Custom request)
- **Required**: Yes
- **Action**: Click the three dots → Go to section based on answer

---

### **SECTION 5: Partnership Inquiries**

#### Field 7: Partnership Type
- **Type**: Multiple choice
- **Question**: "What type of partnership are you interested in?"
- **Options**:
  - Educational collaboration (course/curriculum integration)
  - Location partnership (featured in Tokyo in Film)
  - Content collaboration
  - Sponsorship
  - Other
- **Required**: Yes

#### Field 8: Organization Name
- **Type**: Short answer
- **Question**: "Company/Organization Name"
- **Required**: Yes

#### Field 9: Partnership Details
- **Type**: Paragraph
- **Question**: "Describe your partnership vision"
- **Help text**: "What would this partnership look like? What value would it provide?"
- **Required**: Yes

**After this section** → Go to Section 12 (Final details)

---

### **SECTION 6: Tokyo May 2026 Projects**

**Section Description**: *I'm available in Tokyo during May 2026 for on-site work.*

#### Field 10: Tokyo Services Needed
- **Type**: Checkboxes (allow multiple)
- **Question**: "What services do you need in Tokyo?"
- **Options**:
  - Videography
  - On-site direction
  - Location scouting/guide services
  - Photography
  - Other
- **Required**: Yes

#### Field 11: May 2026 Dates
- **Type**: Short answer
- **Question**: "What dates in May 2026?"
- **Help text**: "Specific dates or general timeframe"
- **Required**: No

#### Field 12: Tokyo Project Description
- **Type**: Paragraph
- **Question**: "Tell me about your project"
- **Required**: Yes

**After this section** → Go to Section 12 (Final details)

---

### **SECTION 7: Travel-Covered Projects (Japan)**

**Section Description**: *For projects outside May 2026 or outside Tokyo, I can travel if expenses are covered.*

#### Field 13: Travel Project Location
- **Type**: Short answer
- **Question**: "Where is the project? (City/region in Japan)"
- **Required**: Yes

#### Field 14: Travel Dates
- **Type**: Short answer
- **Question**: "When do you need me there?"
- **Required**: Yes

#### Field 15: Services Needed (Travel)
- **Type**: Checkboxes
- **Question**: "What services do you need?"
- **Options**:
  - Videography
  - Directing
  - Location scouting/guide
  - Photography
  - Other
- **Required**: Yes

#### Field 16: Travel Project Description
- **Type**: Paragraph
- **Question**: "Describe your project"
- **Required**: Yes

**After this section** → Go to Section 12 (Final details)

---

### **SECTION 8: Custom Request / Something Else**

#### Field 17: Custom Request Description
- **Type**: Paragraph
- **Question**: "Tell me what you're looking for"
- **Help text**: "Describe your needs, timeline, and any other relevant details"
- **Required**: Yes

**After this section** → Go to Section 12 (Final details)

---

### **SECTION 9: Nashville Service Details**

#### Field 18: Nashville Project Description
- **Type**: Paragraph
- **Question**: "Describe your project"
- **Help text**: "Goals, audience, vision, deliverables needed"
- **Required**: Yes

#### Field 19: Project Timeline
- **Type**: Short answer
- **Question**: "When do you need this completed?"
- **Required**: No

**After this section** → Go to Section 12 (Final details)

---

### **SECTION 10: Remote Work Details**

#### Field 20: Remote Services Needed
- **Type**: Checkboxes
- **Question**: "What remote services do you need?"
- **Options**:
  - Video editing
  - Script writing
  - Copyediting
  - Consultation/planning
  - Other
- **Required**: Yes

#### Field 21: Remote Project Details
- **Type**: Paragraph
- **Question**: "Describe your project"
- **Help text**: "What you need, timeline, deliverables"
- **Required**: Yes

**After this section** → Go to Section 12 (Final details)

---

### **SECTION 11: On-Site Travel Work**

#### Field 22: Travel Destination
- **Type**: Short answer
- **Question**: "Where is the project located?"
- **Required**: Yes

#### Field 23: Travel Dates
- **Type**: Short answer
- **Question**: "When do you need me on-site?"
- **Required**: Yes

#### Field 24: Travel Services
- **Type**: Checkboxes
- **Question**: "What services do you need?"
- **Options**:
  - Videography
  - Directing
  - Location scouting
  - Photography
  - Other
- **Required**: Yes

#### Field 25: Travel Project Description
- **Type**: Paragraph
- **Question**: "Describe your project"
- **Required**: Yes

**After this section** → Go to Section 12 (Final details)

---

### **SECTION 12: Final Details & Budget** (Everyone ends here)

#### Field 26: Budget Range
- **Type**: Multiple choice
- **Question**: "What's your budget range?"
- **Options**:
  - Under $1,000
  - $1,000 - $3,000
  - $3,000 - $5,000
  - $5,000 - $10,000
  - $10,000+
  - Not sure / Prefer to discuss
- **Required**: No

#### Field 27: How Did You Hear About Me?
- **Type**: Multiple choice
- **Question**: "How did you find me?"
- **Options**:
  - Instagram (@chaues)
  - Tokyo in Film website
  - Google search
  - Referral from someone
  - Local partner
  - Other
- **Required**: No

#### Field 28: Additional Notes/Message
- **Type**: Paragraph
- **Question**: "Anything else you want me to know?"
- **Help text**: "Questions, special requirements, additional context, etc."
- **Required**: No

---

## Setting Up Section Branching

1. **Create sections**: After adding a field, click the **Add section** button (looks like two rectangles)
2. **Section titles**: Each section heading above (e.g., "Japan-Based Inquiries") should be the section title in Google Forms
3. **Section descriptions**: The italic text in quotes should go in the "Section description" field
4. **Set up branching**: On multiple choice questions with "→ Go to Section X", click the three dots → **Go to section based on answer**
5. **Map each answer** to the specified section number
6. **Test thoroughly**: Use the preview button (eye icon) to test all paths before sharing

## Step 3: Configure Form Settings

1. Click the **Settings** gear icon (top right)
2. Under **Responses**:
   - ✅ Collect email addresses
   - ✅ Limit to 1 response (optional)
   - ✅ Send respondent a copy of their response
3. Under **Presentation**:
   - ✅ Show progress bar
   - Confirmation message: "Thank you! I'll get back to you within 24-48 hours."

## Step 4: Get Your Form URL

1. Click **Send** button (top right)
2. Click the link icon (🔗)
3. Check **Shorten URL** if you want
4. **Copy the URL** - it will look like:
   ```
   https://forms.gle/XXXXXXXXXX
   ```
   or
   ```
   https://docs.google.com/forms/d/e/XXXXXXXXXXX/viewform
   ```

## Step 5: Update landing.html

Replace the contact button URL on line 357:

**BEFORE:**
```html
<a href="#" class="contact-btn">Planning / Guide / Videography</a>
```

**AFTER:**
```html
<a href="YOUR_GOOGLE_FORM_URL_HERE" class="contact-btn" target="_blank" rel="noopener noreferrer">Planning / Guide / Videography</a>
```

## Alternative: Embed the Form

If you want to embed the form directly on your landing page instead of opening in a new tab, see the `embed_google_form.html` example file.

## Email Notifications

To receive email notifications when someone submits the form:

1. Open your Google Form
2. Go to **Responses** tab
3. Click the three dots menu (top right)
4. Select **Get email notifications for new responses**

---

**Next Step**: After creating your form, copy the URL and I'll update your landing.html file with it!
