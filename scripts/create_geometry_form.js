function createGeometryForm() {
    var form = FormApp.create('Geometry Add-On Worksheet');
    form.setDescription('Goal: Add geometric staging to a dialogue scene so the audience can read tension and relationships without defaulting to close-up coverage.');

    // Project Information
    form.addSectionHeaderItem().setTitle('Project Information');
    form.addTextItem().setTitle('Student Name').setRequired(true);
    form.addTextItem().setTitle('Project Title').setRequired(true);

    var stageItem = form.addMultipleChoiceItem();
    stageItem.setTitle('Current Project Stage')
        .setChoices([
            stageItem.createChoice('Planning'),
            stageItem.createChoice('Shot'),
            stageItem.createChoice('Rough Cut'),
            stageItem.createChoice('Near Final')
        ]).setRequired(true);

    form.addTextItem().setTitle('Scene').setRequired(true);
    form.addTextItem().setTitle('Location').setRequired(true);
    form.addParagraphTextItem().setTitle('Characters in scene (list)').setRequired(true);

    // Step 1: Pick the “Geometry Anchor”
    form.addPageBreakItem().setTitle('Step 1: Pick the “Geometry Anchor”')
        .setHelpText('Choose the one thing that must stay readable and will anchor the design.');

    var anchorTypeItem = form.addMultipleChoiceItem();
    anchorTypeItem.setTitle('Anchor Type')
        .setChoices([
            anchorTypeItem.createChoice('Object'),
            anchorTypeItem.createChoice('Exit-Threshold'),
            anchorTypeItem.createChoice('Power Seat'),
            anchorTypeItem.createChoice('Secret-Witness'),
            anchorTypeItem.createChoice('Other')
        ]).setRequired(true);

    form.addTextItem().setTitle('Anchor is:').setRequired(true);

    var framePosItem = form.addMultipleChoiceItem();
    framePosItem.setTitle('Where will it sit in the frame?')
        .setChoices([
            framePosItem.createChoice('Foreground'),
            framePosItem.createChoice('Midground'),
            framePosItem.createChoice('Background')
        ]).setRequired(true);

    // Step 2: Build the First Shape
    form.addPageBreakItem().setTitle('Step 2: Build the First Shape')
        .setHelpText('Pick one base shape and define its points.');

    var shape1TypeItem = form.addMultipleChoiceItem();
    shape1TypeItem.setTitle('Shape 1 Type')
        .setChoices([
            shape1TypeItem.createChoice('Triangle'),
            shape1TypeItem.createChoice('Square (trap)'),
            shape1TypeItem.createChoice('Line (rank)'),
            shape1TypeItem.createChoice('Cluster (pressure)')
        ]).setRequired(true);

    form.addTextItem().setTitle('Shape 1 name').setRequired(true);
    form.addTextItem().setTitle('Point A').setRequired(true);
    form.addTextItem().setTitle('Point B').setRequired(true);
    form.addTextItem().setTitle('Point C').setRequired(true);
    form.addTextItem().setTitle('Point D (Optional)');

    form.addTextItem().setTitle('What is the viewer supposed to look at first?').setRequired(true);

    // Step 3: Lock the Frame Rule
    form.addPageBreakItem().setTitle('Step 3: Lock the Frame Rule')
        .setHelpText('Geometry only works if the camera rule is stable.');

    var ruleItem = form.addMultipleChoiceItem();
    ruleItem.setTitle('Choose one rule')
        .setChoices([
            ruleItem.createChoice('Rule 1: Hold a wide or medium-wide until the shape changes.'),
            ruleItem.createChoice('Rule 2: No reaction cuts unless a new fact appears.'),
            ruleItem.createChoice('Rule 3: Reframe only when a character crosses a boundary (door, corner, table edge).')
        ]).setRequired(true);

    form.addTextItem().setTitle('My rule is (specifics):').setRequired(true);

    // Step 4: Plan the Shape Change
    form.addPageBreakItem().setTitle('Step 4: Plan the Shape Change')
        .setHelpText('A geometry scene needs at least one clear transformation.');

    form.addTextItem().setTitle('Trigger: What causes the shape to change?')
        .setHelpText('Example triggers: entry, object handoff, accusation, reveal, someone backing up.')
        .setRequired(true);

    var shape2TypeItem = form.addMultipleChoiceItem();
    shape2TypeItem.setTitle('Shape 2 Type')
        .setChoices([
            shape2TypeItem.createChoice('Triangle'),
            shape2TypeItem.createChoice('Square'),
            shape2TypeItem.createChoice('Line'),
            shape2TypeItem.createChoice('Cluster')
        ]).setRequired(true);

    var diffItem = form.addCheckboxItem();
    diffItem.setTitle('How does Shape 2 differ from Shape 1?')
        .setChoices([
            diffItem.createChoice('Expands (distance increases)'),
            diffItem.createChoice('Compresses (trap forms)'),
            diffItem.createChoice('Rotates (new dominant angle)'),
            diffItem.createChoice('Splits (two vs one)'),
            diffItem.createChoice('Breaks (one point peels off to anchor object)')
        ]).setRequired(true);

    form.addTextItem().setTitle('Describe the new arrangement in one sentence:').setRequired(true);

    // Step 5: Geometry Beat Map
    form.addPageBreakItem().setTitle('Step 5: Geometry Beat Map')
        .setHelpText('List the scene as shape beats. Keep it simple and countable.');

    // Helper to create the number choices reused 4 times
    function createNumChoices(item) {
        return [item.createChoice('1'), item.createChoice('2'), item.createChoice('3'), item.createChoice('4')];
    }
    function createYesNo(item) {
        return [item.createChoice('Yes'), item.createChoice('No')];
    }

    // Beat 1
    var b1Num = form.addMultipleChoiceItem();
    b1Num.setTitle('Beat 1 (start) - Number of people').setChoices(createNumChoices(b1Num));
    form.addTextItem().setTitle('Beat 1 Shape');
    var b1Anchor = form.addMultipleChoiceItem();
    b1Anchor.setTitle('Beat 1 Anchor visible?').setChoices(createYesNo(b1Anchor));

    // Beat 2
    var b2Num = form.addMultipleChoiceItem();
    b2Num.setTitle('Beat 2 (pressure rises) - Number of people').setChoices(createNumChoices(b2Num));
    form.addTextItem().setTitle('Beat 2 Shape');
    var b2Anchor = form.addMultipleChoiceItem();
    b2Anchor.setTitle('Beat 2 Anchor visible?').setChoices(createYesNo(b2Anchor));

    // Beat 3
    var b3Num = form.addMultipleChoiceItem();
    b3Num.setTitle('Beat 3 (peak) - Number of people').setChoices(createNumChoices(b3Num));
    form.addTextItem().setTitle('Beat 3 Shape');
    var b3Anchor = form.addMultipleChoiceItem();
    b3Anchor.setTitle('Beat 3 Anchor visible?').setChoices(createYesNo(b3Anchor));

    // Beat 4
    var b4Num = form.addMultipleChoiceItem();
    b4Num.setTitle('Beat 4 (release) - Number of people').setChoices(createNumChoices(b4Num));
    form.addTextItem().setTitle('Beat 4 Shape');
    var b4Anchor = form.addMultipleChoiceItem();
    b4Anchor.setTitle('Beat 4 Anchor visible?').setChoices(createYesNo(b4Anchor));

    var arcItem = form.addMultipleChoiceItem();
    arcItem.setTitle('Are you using the clean "geometry arc" (1 -> 2 -> 3 -> 2 -> 1)?')
        .setChoices(createYesNo(arcItem));

    // Step 6: Blocking Instructions
    form.addPageBreakItem().setTitle('Step 6: Blocking Instructions (Concrete Moves Only)')
        .setHelpText('Write the moves that create the shapes. No psychology, just actions.');

    form.addParagraphTextItem().setTitle('Blocking Moves').setRequired(true);

    // Step 7: Composition Checks
    form.addPageBreakItem().setTitle('Step 7: Composition Checks');

    form.addTextItem().setTitle('Triangle Check (if applicable): Who is Point A looking at?');
    form.addTextItem().setTitle('Triangle Check: Who is Point B looking at?');
    form.addTextItem().setTitle('Triangle Check: What is the third point (object or person)?');

    form.addTextItem().setTitle('Square Trap Check (if applicable): What frames the trapped character?')
        .setHelpText('Doorway / wall corner / table edge / window / bodies / other');

    var clarityItem = form.addMultipleChoiceItem();
    clarityItem.setTitle('Clarity Check: In one wide frame, can we read all points of the shape?')
        .setChoices(createYesNo(clarityItem)).setRequired(true);

    form.addTextItem().setTitle('If no, what must change?');

    // Final Confirmation
    form.addPageBreakItem().setTitle('Final Confirmation');

    form.addParagraphTextItem().setTitle('Fill in the blanks: This scene adds geometry by staging [shape] around [anchor], then changing it to [new shape] when [trigger] happens.')
        .setRequired(true);

    Logger.log('Published URL: ' + form.getPublishedUrl());
    Logger.log('Edit URL: ' + form.getEditUrl());
}
