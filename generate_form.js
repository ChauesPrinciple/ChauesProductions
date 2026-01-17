function createChauesContactForm() {
    // 1. Create the form
    var form = FormApp.create('Chaues Productions - Smart Contact Form');
    form.setDescription('Get in touch for planning, guide services, or videography inquiries.');
    form.setProgressBar(true);
    form.setCollectEmail(true);

    // --- CREATE ALL SECTIONS FIRST (to allow navigation routing) ---
    var section1 = form.addPageBreakItem().setTitle('Contact Information'); // Technically section 2 visually, but we start adding questions to the main body first

    // Actually, FormApp adds items sequentially. We need to creates pages as we go 
    // or create page breaks to define sections.
    // Strategy: Add PageBreak = New Section. 
    // We need references to these breaks to set navigation.

    // Let's create the PAGE BREAKS first so we can route to them.
    // Note: The form starts with "Section 1".

    // We will build the form linearly and save references to pages to set navigation later.

    // --- SECTION 1: CONTACT INFO ---
    // (Items added to 'form' go into Section 1 initially)
    var nameItem = form.addTextItem().setTitle('Your Name').setRequired(true);
    // Email is collected automatically via setCollectEmail(true) or we can add a field
    var emailItem = form.addTextItem().setTitle('Your Email Address').setRequired(true);

    // Location Question (Routing)
    var locationRouting = form.addMultipleChoiceItem()
        .setTitle('Where are you located?')
        .setHelpText('This helps me route you to the right options')
        .setRequired(true);

    // --- SECTION 2: JAPAN INQUIRIES ---
    var sectionJapan = form.addPageBreakItem().setTitle('Japan-Based Inquiries')
        .setHelpText('Are you a company/organization in Japan interested in partnering with Tokyo in Film? Select "Partnership" below. Looking to hire me for on-site work in Tokyo? I\'m available in May 2026, or if you can cover travel expenses for other dates.');

    var japanInquiryType = form.addMultipleChoiceItem()
        .setTitle('What are you interested in?')
        .setRequired(true);

    // --- SECTION 3: NASHVILLE INQUIRIES ---
    var sectionNashville = form.addPageBreakItem().setTitle('Nashville-Based Inquiries')
        .setHelpText('I\'m based in Nashville and available for local projects year-round.');

    var nashvilleServiceType = form.addMultipleChoiceItem()
        .setTitle('What type of project do you need?')
        .setRequired(true);

    // --- SECTION 4: OTHER LOCATIONS ---
    var sectionOther = form.addPageBreakItem().setTitle('Other Locations')
        .setHelpText('For projects outside Nashville or Japan, I\'m available remotely (editing, writing) or on-site if travel is covered.');

    var otherServiceType = form.addMultipleChoiceItem()
        .setTitle('What type of work do you need?')
        .setRequired(true);

    // --- SECTION 5: PARTNERSHIP ---
    var sectionPartnership = form.addPageBreakItem().setTitle('Partnership Inquiries');
    form.addMultipleChoiceItem().setTitle('What type of partnership are you interested in?')
        .setChoiceValues(['Educational collaboration (course/curriculum integration)', 'Location partnership (featured in Tokyo in Film)', 'Content collaboration', 'Sponsorship', 'Other'])
        .setRequired(true);
    form.addTextItem().setTitle('Company/Organization Name').setRequired(true);
    form.addParagraphTextItem().setTitle('Describe your partnership vision').setHelpText('What would this partnership look like? What value would it provide?').setRequired(true);

    // --- SECTION 6: TOKYO MAY 2026 ---
    var sectionTokyoMay = form.addPageBreakItem().setTitle('Tokyo May 2026 Projects')
        .setHelpText('I\'m available in Tokyo during May 2026 for on-site work.');
    form.addCheckboxItem().setTitle('What services do you need in Tokyo?')
        .setChoiceValues(['Videography', 'On-site direction', 'Location scouting/guide services', 'Photography', 'Other'])
        .setRequired(true);
    form.addTextItem().setTitle('What dates in May 2026?').setHelpText('Specific dates or general timeframe');
    form.addParagraphTextItem().setTitle('Tell me about your project').setRequired(true);

    // --- SECTION 7: TRAVEL COVERED (JAPAN) ---
    var sectionTravelJapan = form.addPageBreakItem().setTitle('Travel-Covered Projects (Japan)')
        .setHelpText('For projects outside May 2026 or outside Tokyo, I can travel if expenses are covered.');
    form.addTextItem().setTitle('Where is the project? (City/region in Japan)').setRequired(true);
    form.addTextItem().setTitle('When do you need me there?').setRequired(true);
    form.addCheckboxItem().setTitle('What services do you need?')
        .setChoiceValues(['Videography', 'Directing', 'Location scouting/guide', 'Photography', 'Other'])
        .setRequired(true);
    form.addParagraphTextItem().setTitle('Describe your project').setRequired(true);

    // --- SECTION 8: CUSTOM REQUEST ---
    var sectionCustom = form.addPageBreakItem().setTitle('Custom Request / Something Else');
    form.addParagraphTextItem().setTitle('Tell me what you\'re looking for').setHelpText('Describe your needs, timeline, and any other relevant details').setRequired(true);

    // --- SECTION 9: NASHVILLE DETAILS ---
    var sectionNashvilleDetails = form.addPageBreakItem().setTitle('Nashville Service Details');
    form.addParagraphTextItem().setTitle('Describe your project').setHelpText('Goals, audience, vision, deliverables needed').setRequired(true);
    form.addTextItem().setTitle('When do you need this completed?');

    // --- SECTION 10: REMOTE DETAILS ---
    var sectionRemote = form.addPageBreakItem().setTitle('Remote Work Details');
    form.addCheckboxItem().setTitle('What remote services do you need?')
        .setChoiceValues(['Video editing', 'Script writing', 'Copyediting', 'Consultation/planning', 'Other'])
        .setRequired(true);
    form.addParagraphTextItem().setTitle('Describe your project').setHelpText('What you need, timeline, deliverables').setRequired(true);

    // --- SECTION 11: ON-SITE TRAVEL DETAILS ---
    var sectionTravelGeneral = form.addPageBreakItem().setTitle('On-Site Travel Work');
    form.addTextItem().setTitle('Where is the project located?').setRequired(true);
    form.addTextItem().setTitle('When do you need me on-site?').setRequired(true);
    form.addCheckboxItem().setTitle('What services do you need?')
        .setChoiceValues(['Videography', 'Directing', 'Location scouting', 'Photography', 'Other'])
        .setRequired(true);
    form.addParagraphTextItem().setTitle('Describe your project').setRequired(true);

    // --- SECTION 12: FINAL DETAILS (Destination for everyone) ---
    var sectionFinal = form.addPageBreakItem().setTitle('Final Details & Budget');
    form.addMultipleChoiceItem().setTitle('What\'s your budget range?')
        .setChoiceValues(['Under $1,000', '$1,000 - $3,000', '$3,000 - $5,000', '$5,000 - $10,000', '$10,000+', 'Not sure / Prefer to discuss']);

    form.addMultipleChoiceItem().setTitle('How did you find me?')
        .setChoiceValues(['Instagram (@chaues)', 'Tokyo in Film website', 'Google search', 'Referral from someone', 'Local partner', 'Other']);

    form.addParagraphTextItem().setTitle('Anything else you want me to know?').setHelpText('Questions, special requirements, additional context, etc.');


    // --- SETTING UP NAVIGATION ROUTING (Logic) ---

    // Section 1 -> Location Routing
    locationRouting.setChoices([
        locationRouting.createChoice('Japan', sectionJapan),
        locationRouting.createChoice('Nashville, TN', sectionNashville),
        locationRouting.createChoice('Other', sectionOther)
    ]);

    // Section 2 (Japan) -> Inquiry Type Routing
    japanInquiryType.setChoices([
        japanInquiryType.createChoice('Partnership with Tokyo in Film course', sectionPartnership),
        japanInquiryType.createChoice('Hiring for May 2026 project in Tokyo', sectionTokyoMay),
        japanInquiryType.createChoice('Hiring with travel coverage', sectionTravelJapan),
        japanInquiryType.createChoice('Something else', sectionCustom)
    ]);

    // Section 3 (Nashville) -> Service Packages Routing
    nashvilleServiceType.setChoices([
        nashvilleServiceType.createChoice('Videography Package (shoot only)', sectionNashvilleDetails),
        nashvilleServiceType.createChoice('Full Production (shoot + edit + direction)', sectionNashvilleDetails),
        nashvilleServiceType.createChoice('Editing Only (you provide footage)', sectionNashvilleDetails),
        nashvilleServiceType.createChoice('Writing/Copyediting (scripts, content)', sectionNashvilleDetails),
        nashvilleServiceType.createChoice('Consultation/Planning (pre-production)', sectionNashvilleDetails),
        nashvilleServiceType.createChoice('Custom Package', sectionCustom)
    ]);

    // Section 4 (Other) -> Remote/OnSite Routing
    otherServiceType.setChoices([
        otherServiceType.createChoice('Remote work (editing, writing, consultation)', sectionRemote),
        otherServiceType.createChoice('On-site work (I travel, you cover expenses)', sectionTravelGeneral),
        otherServiceType.createChoice('Not sure / Custom request', sectionCustom)
    ]);

    // --- SETTING DESTINATIONS TO FINAL SECTION ---
    // Any section that shouldn't just "continue to next" needs a destination set

    sectionPartnership.setGoToPage(sectionFinal);
    sectionTokyoMay.setGoToPage(sectionFinal);
    sectionTravelJapan.setGoToPage(sectionFinal);
    sectionCustom.setGoToPage(sectionFinal);
    sectionNashvilleDetails.setGoToPage(sectionFinal);
    sectionRemote.setGoToPage(sectionFinal);
    sectionTravelGeneral.setGoToPage(sectionFinal);

    // Log the URL
    Logger.log('Form created: ' + form.getEditUrl());
    Logger.log('Share URL: ' + form.getPublishedUrl());
}
