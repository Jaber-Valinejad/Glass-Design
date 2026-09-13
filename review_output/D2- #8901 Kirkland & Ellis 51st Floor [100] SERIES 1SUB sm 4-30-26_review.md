# Design Review: D2- #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB sm 4-30-26.pdf


## Page 1

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.1 (0.98), #8859 CIBC Int [100] Series FabInstall (1).pdf p.1 (0.94), #8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.1 (0.93), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10 (0.89), #8859 CIBC Int [100] Series FabInstall (1).pdf p.7 (0.88), #8859 CIBC Int [100] Series FabInstall (1).pdf p.10 (0.88)

## Summary
The design sheet largely conforms to the provided baseline standards by including the expected cover sheet elements. However, several details and specifications are either missing or inconsistent, requiring clarification.

## Issues Found

1.  **Missing Infill Type Specification for GL3-GL7:** The "Infill Schedule" on the design sheet lists marks GL3 through GL7 with the description "ARCH GL". This is a generic placeholder and does not specify the actual glass type, thickness, or any specific properties required. This is critical for fabrication and material procurement.
    *   **Why it matters:** Inability to procure correct materials, potential for incorrect glass installation, and deviation from expected specification.
    *   **Baseline Conflict:** Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.1] also has this issue, but it is noted as a potential area for clarification in its own description. Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.1] also lists placeholders in its symbols section for GL3-GL5 but omits them from the schedule. Baseline reference [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.1] does not show an infill schedule with placeholder types.

2.  **Undocumented "NBSGC" Suffix:** The suffix "-NBSGC-" is used repeatedly in Detail V5 (on page V102 of the referenced design sheet) for "METAL STUD", "BLOCKING", and "INTERIOR FINISH". This abbreviation is not defined on the design sheet, hindering clear understanding of who is responsible for these components or their specific requirements.
    *   **Why it matters:** Ambiguity in responsibility for critical structural and finish components, potential for incorrect installation or material selection.
    *   **Baseline Conflict:** Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.10] contains the same undefined "-NBSGC-" suffix, indicating this is a recurring issue or a standard practice for this specific project that needs clarification. Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10] also uses "-NBSGC-" for multiple components without definition.

3.  **Inconsistent Table Formatting in "Infill Schedule":** On the design sheet, the "Infill Schedule" table has the "MARK" column empty, but the text "GL4" is presented in a bubble to the left of the "INFILL DESCRIPTION" column. This inconsistent formatting makes it difficult to clearly identify the mark associated with the described infill.
    *   **Why it matters:** Potential for misidentification of infill types, impacting fabrication and installation accuracy.
    *   **Baseline Conflict:** Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.1] contains a similar issue in its Table of Contents and Symbols section where infill types are listed but not fully described in the schedule. The design sheet's specific formatting issue is unique.

4.  **Unclear Framing System Designation:** The "Framing System(s) Used" section on the design sheet lists "-FHC PASS THRU WINDOW SNOXXOBAC (OXXO)". The term "SNOXXOBAC" appears to be a proprietary or unusual product designation, and its meaning or full context is not clear from this sheet.
    *   **Why it matters:** Lack of clarity on the specific system being used could lead to fabrication or installation errors if the designation has specific technical implications.
    *   **Baseline Conflict:** Baseline reference [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.1] shares this same framing system designation, highlighting it as a project-specific term that needs to be understood.

5.  **Missing Dimensions in Details V5, V6, and V7:** Details V5, V6, and V7 on page V102 of the design sheet include dimension lines for "WP TO WP", "GLASS SIZE", and "DOOR SIZE", but the numerical values for these dimensions are missing.
    *   **Why it matters:** Critical dimensions for fabrication and installation are absent, leading to potential guesswork and errors.
    *   **Baseline Conflict:** Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10] (which is page V102 from the same project as the design sheet) lists these same dimension lines without numerical values, indicating this is a consistent omission within the detail sheets for this project. Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.10] also shows similar dimensions without values.

6.  **Deferred Glass Type Specification:** The note "SEE ELEVATION FOR TYPE" accompanies the "1/2" GLASS" callout in Details V5, V6, and V7 (page V102 of the design sheet). The specific type of glass (e.g., tempered, laminated, clear, low-iron) is not detailed on this sheet.
    *   **Why it matters:** The specific glass properties are critical for performance (safety, structural, aesthetic) and must be clearly defined for procurement and installation.
    *   **Baseline Conflict:** Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10] (page V102) has this exact same deferral note, indicating this is how the specification is handled across these project details. Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.10] also shows similar deferrals.

7.  **Revision Date Discrepancy in Title Block:** The "Date" in the main title block is "11/14/25" and the "REV 01 DATE" is "02/06/26". While both are in the future relative to the current year (2024), the specific day difference for a revision indicates a potential issue with the date input or timeline management.
    *   **Why it matters:** Potential confusion regarding the active drawing date and the date of revisions, impacting workflow and documentation accuracy.
    *   **Baseline Conflict:** Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.7] also shows a date discrepancy between the main title block and a revision date (11/14/25 vs. 02/06/26). This suggests a pattern of date entry or project timeline issues.

## Items That Match the Standard

*   The design sheet, as a cover sheet, includes all the expected general information sections such as project identification, company information, framing systems, materials, performance standards, notes, symbols, abbreviations, and a table of contents.
*   The inclusion of a "Drawing Release Record" and an "Architectural Dwg. Ref. Set" section aligns with standard shop drawing submittal practices.
*   The provision of a "Door Swing Diagram" and "Infill Schedule" are also typical and conform to good practice.

## Open Questions / Needs Clarification

*   **Definition of "NBSGC":** Clarification is needed on what "NBSGC" stands for and the responsibility assigned to it for components like metal studs, blocking, and interior finishes.
*   **Specific Infill Types for GL3-GL7:** Detailed specifications for the infill types corresponding to marks GL3 through GL7 are required.
*   **Meaning of "SNOXXOBAC":** The exact technical meaning and implications of the "SNOXXOBAC" designation within the "Framing System(s) Used" section need to be understood.
*   **"WP TO WP", "GLASS SIZE", "DOOR SIZE" Dimensions:** The specific numerical values for these dimensions are required for accurate fabrication.
*   **Exact Glass Specifications:** The specific type of "1/2" GLASS" (e.g., tempered, laminated, thickness, coatings) needs to be clearly defined, as deferred to the elevations.
*   **Date Clarification:** The reason for the discrepancy between the main drawing date and the revision date needs to be clarified to ensure accurate project tracking.


## Page 2

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.2 (0.98), #8859 CIBC Int [100] Series FabInstall (1).pdf p.2 (0.94), #8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.2 (0.93), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10 (0.87), #8859 CIBC Int [100] Series FabInstall (1).pdf p.10 (0.87), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8 (0.86)

## Summary
The fastener index for the interior glazing system is mostly consistent with standard practices and baseline references, with a few minor areas needing clarification regarding the sourcing and specific application of one of the fasteners.

## Issues Found
1.  **Ambiguous Part Numbering for Fastener #2:** Fastener #2, described as a "#10/#12 GREEN MASONRY PLUG *PLASTIC", shares the exact same PART# (FASTENAL #50985) as Fastener #5 in baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.2]. However, Fastener #2 on the design sheet appears visually as a plug or anchor, while Fastener #5 in the baseline reference is also described as a "Green Masonry Plug" but is distinct from the image presented for Fastener #2 on the design sheet. This identical part number for two seemingly distinct components (a plug/anchor and a different plug type) could lead to ordering or installation errors.
    *   **Why it matters:** Incorrect fastener selection can lead to improper anchorage, compromising the integrity and safety of the glazing system.
    *   **Baseline Support:** [#8859 CIBC Int [100] Series FabInstall (1).pdf p.2] shows this same part number duplication for different items.

2.  **Unclear Sourcing/Inventory Note for Fastener #2:** The note "SGC INVENTORY" is checked for Fastener #2. While this indicates an available stock item, its placement and form do not integrate seamlessly with the descriptive text. It would be more standard for inventory status to be a separate field or noted more explicitly within the description if it affects material specification, rather than a simple checkmark.
    *   **Why it matters:** Clarity on fastener sourcing is important for procurement and project management. While not a direct constructability issue, it can impact project timelines if the "inventory" status is misunderstood or not confirmed.
    *   **Baseline Support:** Baseline references [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.2] and [#8859 CIBC Int [100] Series FabInstall (1).pdf p.2] also utilize "SGC INVENTORY" notes, but the design sheet's implementation with a checkmark is a minor presentation variation.

3.  **Inconsistent Image and Description for Fastener #2:** The image for Fastener #2 depicts a plug or anchor, while the descriptive text for Fasteners #1 and #3 uses "PFH TYPE-A SMS" which implies a screw. Although Fastener #2 is a plug intended for use with a screw, the direct comparison of images between screws and plugs in a fastener index could be visually confusing without clearer distinction. Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.2] also presents a similar juxtaposition of screw images and a plug image.
    *   **Why it matters:** While the descriptions differentiate the items, placing a plug image alongside screw images can be jarring if not clearly understood as different component types. This is a minor clarity issue.
    *   **Baseline Support:** [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.2] demonstrates this visual grouping as well.

## Items That Match the Standard
*   The overall format of the fastener index, including the columns for FASTENER#, IMAGE, PART#, and DESCRIPTION, aligns with standard practice and is consistent across multiple baseline references (e.g., [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.2], [#8859 CIBC Int [100] Series FabInstall (1).pdf p.2], [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.2]).
*   The descriptions for the screws (Fasteners #1 and #3) provide specific details such as diameter, thread count, length, head type, screw type, and material, which is comprehensive and consistent with baseline references (e.g., [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.2], [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.2]).
*   The use of industry-standard abbreviations for screw types and materials (e.g., PFH, SMS, *18-8SS) is consistent with baseline examples.

## Open Questions / Needs Clarification
*   Clarification is needed regarding the duplicate PART# (FASTENAL #50985) for Fastener #2 and Fastener #5 in baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.2]. It is essential to confirm if these are truly the same part or if there is an error in the provided part numbers to avoid procurement errors.
*   The red dashed rectangle around "#FA083" and "FASTENAL #50985" for Fastener #2 on the design sheet itself is not explicitly explained. Its purpose (e.g., highlight, markup, query) should be clarified.


## Page 3

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.3 (0.97), #8859 CIBC Int [100] Series FabInstall (1).pdf p.3 (0.90), #8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.3 (0.90), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5 (0.87), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4 (0.87), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.1 (0.86)

## Summary
The design sheet for Level 51 Finish Plan (P101) generally aligns with standard architectural floor plan conventions for depicting room layouts and circulation. However, it lacks specific detail regarding glazing systems and critical information required for a shop drawing submittal, such as material specifications and detailed section callouts.

## Issues Found

1.  **Lack of Glazing System Specification:** The design sheet (P101) depicts interior partitions with thin lines suggesting glass, but it does not explicitly call out that these are glazing systems, nor does it specify materials, frame types, finishes, or glass specifications. This is a critical omission for a glazing shop drawing submittal.
    *   **Why it Matters:** Constructability, quality of finish, acoustic performance, and aesthetics depend on these specifications. Without them, the intent of the glass partitions cannot be confirmed or executed properly.
    *   **Baseline Reference:** Standard practice, as seen in references like [#8859 CIBC Int [100] Series FabInstall (1).pdf p.3] and [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.3], is to clearly indicate glass partitions (e.g., with cross-hatching, specific legends) and often provides references to elevation/detail sheets that define the framing and glass types. The design sheet here is a basic floor plan lacking this crucial glazing-specific information.

2.  **Ambiguous Elevator Labeling:** Two of the four elevator shafts within the 5100 ELEVATOR LOBBY are identically labeled "3 E102".
    *   **Why it Matters:** This creates confusion and ambiguity in identifying specific elevator cabs, potentially leading to operational issues or miscommunication during construction.
    *   **Baseline Reference:** Standard practice dictates unique identification for each elevator shaft. While not explicitly detailed in the provided floor plans, standard elevator system drawings and naming conventions would ensure distinct labels. Reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] shows distinct numbering and labeling for elevator shafts in its elevation drawings (e.g., "1 E101", "2 E101", "3 E102", "3 E102" which itself has a double labeling).

3.  **Future Date in Title Block:** The "DATE: 5/4/26" in the title block is a future date.
    *   **Why it Matters:** While not a direct construction issue, it is an inconsistency that raises questions about the drawing's currency and accuracy.
    *   **Baseline Reference:** All baseline references show current or past dates relevant to a submittal process (e.g., [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.3] with "DATE: 5/4/26", [#8859 CIBC Int [100] Series FabInstall (1).pdf p.3] with "DATE 11/14/25", [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.3] with "DATE: 12/23/25"). The future date on the design sheet is unusual.

## Items That Match the Standard

*   The floor plan effectively depicts room layouts, labels, and circulation paths, consistent with architectural floor plan standards.
*   Structural grid lines are clearly indicated.
*   Standard architectural symbols for doors and stairs are used.

## Open Questions / Needs Clarification

*   The specific meaning of abbreviations like "ASSOC.", "DBL ASSOC.", and "PA WKST" for rooms requires a legend or explicit definition.
*   The circular callouts with numbers and "E101" or "E102" (e.g., '1 E101', '2 E101', '3 E102') need clarification regarding their purpose (e.g., specific elevator zone, control point, or maintenance access).
*   The intended material and finish for the thin-line partitions (implied glass) needs to be specified. This would typically be detailed on elevation or specification sheets associated with this floor plan.


## Page 4

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4 (0.98), #8859 CIBC Int [100] Series FabInstall (1).pdf p.4 (0.93), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5 (0.93), #8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.4 (0.91), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.9 (0.90), #8859 CIBC Int [100] Series FabInstall (1).pdf p.6 (0.90)

## Summary
The design sheet presents elevations for elevator lobbies with glass walls. While generally well-defined, there are several discrepancies and missing details compared to standard practices and baseline references, particularly concerning dimension verification, hardware standardization, and clarity of specific installation details.

## Issues Found

1.  **Overridden Dimension Discrepancy:** The design sheet has a redline comment: "WHY WAS DIM OVERRIDDEN? IT SHOULD BE 15 5/8" WP TO WP BETWEEN THE TRIM OVER THE DOORS." This indicates a direct conflict with an existing dimension on the drawing and implies a potential error in the proposed revision or fabrication data. This matters for constructability and ensuring the correct fit of elements around the elevator doors.
    *   *Baseline Support:* This is an explicit markup on the design sheet itself, highlighting an internal inconsistency.
2.  **Unclear Glass Type Usage:** The legend defines GL1 as "7/16" Acid Etch Laminated Mirror" and GL2 as "1/2" Clear Tempered Glass." However, all glass panels in the ELEVATION-EAST and ELEVATION-WEST are labeled "GL1." The referenced baseline drawings [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] and [#8859 CIBC Int [100] Series FabInstall (1).pdf p.6] clearly show GL1 (Backpainted Galaxy) or GL2 (Clear Tempered) being used specifically in different areas. The consistent use of GL1 on the design sheet for all panels, when GL2 is defined, raises questions about the intended glass specification for these elevations and whether the correct glass type is being called out for all applications. This impacts aesthetics and material ordering.
    *   *Baseline Support:* [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] and [#8859 CIBC Int [100] Series FabInstall (1).pdf p.6] show specific uses of GL1 and GL2, implying distinct applications are intended.
3.  **Ambiguous Red Dashed Line Markup:** In ELEVATION-EAST, a wavy red dashed line encloses a portion of a glass panel. There is no accompanying note or legend to explain its purpose. This is a critical omission as it could relate to a specific finish, cut-out, or fabrication requirement, impacting quality and appearance.
    *   *Baseline Support:* While baselines don't typically have undefined markups, the absence of explanation for a visual markup represents a deviation from clear communication standards seen in baseline drawings like [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] which are generally clear in their notations.
4.  **Unverified "DLOS" Note:** The note "WE DO NOT NEED THESE STRINGS OF DIMS. THERE ARE NO DLOS. KEEP IF YOU WANT." is vague. While "DLOS" likely refers to Daylight Openings, the instruction to disregard dimensions without clear justification or clarification of what constitutes a "string of dims" can lead to misinterpretation or omission of critical dimensional data during fabrication or installation. This impacts constructability.
    *   *Baseline Support:* Baseline drawings like [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] and [#8859 CIBC Int [100] Series FabInstall (1).pdf p.6] are generally precise with dimensions and notes, emphasizing the need for clarity where dimensions are provided.
5.  **"CHECK PICK POINT" Markup:** A redline comment "CHECK PICK POINT" with an arrow pointing to a location on ELEVATION-EAST indicates a potential issue or required verification point that is not further elaborated. This suggests a possible discrepancy or a need for on-site confirmation that is not clearly defined within the drawing itself, impacting constructability and accuracy.
    *   *Baseline Support:* This is an explicit markup on the design sheet itself.
6.  **Unclear "B.O. CEILING 62"" Dimension:** In ELEVATION-EAST, the dimension "B.O. CEILING 62"" appears in relation to a recessed opening. Its reference point and the ceiling it refers to (general lobby ceiling or a localized soffit) are not clearly defined, potentially leading to confusion during installation of adjacent elements.
    *   *Baseline Support:* Baselines like [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] show dimensions to recognized building elements (like CEILING, B.O. TRIM) with clear relationships. This dimension's lack of clear referencing makes it ambiguous.
7.  **Inconsistent Material Callouts for Elevations:** While GL1 is defined as "7/16" Acid Etch Laminated Mirror" and GL2 as "1/2" Clear Tempered Glass," the elevations exclusively show GL1. Baseline drawings like [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] and [#8859 CIBC Int [100] Series FabInstall (1).pdf p.6] demonstrate clear differentiation and specific application of different glass types (GL1, GL2) within elevations and lobbies. The sole use of GL1 here might be an error, or GL2 might be intended for other, unspecified areas. This is critical for material specification and procurement.
    *   *Baseline Support:* [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4] and [#8859 CIBC Int [100] Series FabInstall (1).pdf p.6] show clear, distinct usage of GL1 and GL2.

## Items That Match the Standard

*   The overall layout and format of the elevation drawings align with standard shop drawing practices, clearly delineating views, components, and dimensions.
*   The use of detail callouts (H1, V1, etc.) referencing other sheets (H101, V101) is a standard and effective method for providing detailed information.
*   The title block information is comprehensive, including project details, drawing information, and company contacts, consistent with baseline examples like [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4].
*   The clear definition of glass types in the legend is a good practice, as seen in baseline drawings.
*   The note to "VERIFY DIMENSIONS IN FIELD" is a standard and crucial disclaimer.

## Open Questions / Needs Clarification

*   The exact material and finish of the general framing elements (vertical and horizontal members) are not specified on this elevation sheet. This information is expected to be found on referenced detail sheets (H101, V101) but should ideally be summarized or alluded to in elevation views where possible.
*   The purpose and nature of the wavy red dashed line in ELEVATION-EAST require clarification from the designer.
*   The meaning of the blue dot in the center of the drawing is unclear.
*   Further detail is needed on the "OVERRIDDEN DIM" mentioned in the redline comment, including the correct proposed dimension and the reasoning behind the original override.
*   Clarification on the intended use of GL2 (1/2" Clear Tempered Glass) is needed, as it is defined but not explicitly called out on the elevations where GL1 (Mirror) is exclusively shown.


## Page 5

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5 (0.97), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.4 (0.94), #8859 CIBC Int [100] Series FabInstall (1).pdf p.6 (0.91), #8859 CIBC Int [100] Series FabInstall (1).pdf p.4 (0.91), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10 (0.90), #8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.4 (0.90)

## Summary
The design sheet E102 largely conforms to standard glazing practices and matches the intent of similar baseline details for elevator lobby glazing systems. However, minor inconsistencies in dimensional clarity and material specification referencing exist.

## Issues Found
1.  **Glass Type for Doors Not Explicitly Specified:** The elevation clearly labels the fixed sidelites as GL2 (1/2" Clear Tempered Glass) but does not explicitly label the glass within the double door opening with a GL type. While it's implied to be the same, for absolute clarity and QA, the door glass should also be tagged GL2.
    *   **Why it matters:** Ensures the correct glass type is used for the doors, crucial for safety and aesthetic consistency.
    *   **Baseline Reference:** Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5] shows similar systems where door glass is implied or labeled consistently with sidelites. Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.6] shows door glass explicitly labeled as GL2.

2.  **Ambiguity of "B.O.D." Dimension:** The dimension labeled "B.O.D. 3"" is placed near the bottom of the elevation. While likely referring to the "Bottom of Door," its exact reference point and clarity could be improved by more explicit labeling or by tying it directly to the door panel's edge.
    *   **Why it matters:** Ensures precise installation height and clearance at the bottom of the door.
    *   **Baseline Reference:** Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5] uses "BOD" notation for door bottom, showing it's a standard notation, but placement and clarity can vary.

3.  **Lack of Explicit Framing Material Specification:** The elevations rely on component tags (H#, V#) to reference detailed framing conditions on other sheets. However, this elevation sheet alone does not explicitly state the material or finish for the overall framing system (e.g., anodized aluminum, stainless steel).
    *   **Why it matters:** Critical for architectural coordination, finish quality, and potential material compatibility issues.
    *   **Baseline Reference:** Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5] also relies on component tags for framing. However, other baseline sheets like [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.4] show frame sections or at least mention frame types in context even on elevation views.

4.  **Inconsistency in "WP TO WP" Dimensions for Rough Opening:** The sheet states "104" [8'-8"] ROUGH OPENING" and then "104" WP TO WP" for the same vertical dimension. While often related, the distinction between a structural rough opening and a work point-to-work point dimension should be clearer if they are intended to be identical. Typically, WP to WP refers to the installed frame or panel dimensions.
    *   **Why it matters:** Potential confusion during field verification and installation regarding what dimension to adhere to – the rough structural opening or the final installed component limits.
    *   **Baseline Reference:** Baseline reference [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5] uses "ROUGH OPENING" and "WP TO WP" as distinct but related dimensions. Baseline reference [#8859 CIBC Int [100] Series FabInstall (1).pdf p.6] also distinguishes between these.

## Items That Match the Standard
*   The overall layout and clarity of the elevation view are good, showing multiple door and sidelite configurations.
*   The use of standard notations like DLO (Daylight Opening), WP TO WP (Work Point to Work Point), and TYP (Typical) is consistent with industry practice.
*   The referencing of specific detail sheets (H#, V#) for framing conditions is standard for elevation drawings.
*   The presence of the "ALL DIMENSIONS TO BE VERIFIED IN FIELD BY SGC PRIOR TO FABRICATION" note is a crucial standard practice for glass submittals.
*   The general glass type (GL2: 1/2" Clear Tempered Glass) for the sidelites is clearly indicated.

## Open Questions / Needs Clarification
*   The specific type and finish of the framing members (e.g., aluminum extrusion profiles, anodize color, or stainless steel cladding) are not detailed on this elevation sheet and rely entirely on referenced detail sheets or specifications not provided here.
*   The exact nature and location of the "3/16" ± TYP" dimension near the bottom center of the elevation (adjacent to "B.O.D.") is not fully clear from the drawing alone. It could refer to glazing stops, clearances, or a frame member dimension.
*   The circular tags like "5101" and "5130" associated with H5 are not explained on this sheet and require reference to the drawings where these numbers are defined.


## Page 6

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6 (0.96), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7 (0.93), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.9 (0.92), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8 (0.91), #8859 CIBC Int [100] Series FabInstall (1).pdf p.7 (0.91), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5 (0.90)

## Summary
The submitted design sheet (H101) for Kirkland & Ellis largely conforms to standard glazing practices and detail conventions seen in the baseline references. However, a significant inconsistency exists in the labeling and depicted detail of "Elevator Head Detail H3."

## Issues Found

1.  **Inconsistent Detail Labeling and Depiction in H3:** Detail H3 is labeled "ELEVATOR HEAD DETAIL @ BACK PAINTED GLASS" but visually depicts a sill condition with setting blocks at the bottom of the glass resting on a head plate, which functions as a sill. Head details do not typically include setting blocks or a sill plate at the top. This is a critical labeling error that could lead to misinterpretation during fabrication or installation.
    *   **Why it matters:** Mislabeling can cause confusion and errors in construction, potentially leading to incorrect installation of the glazing system, impacting performance, aesthetics, and safety.
    *   **Baseline Reference:** Although no direct counter-example detail is provided in the baseline for an "elevator head," standard glazing practice dictates that head details are at the top and sill details are at the bottom. This detail's configuration (setting blocks at the bottom, resting on a plate) is characteristic of a sill. The other elevator details (V2, V3 on V101) show more typical jamb/head/sill conditions that don't present this specific contradiction.

2.  **Undefined "-NBSGC-" Abbreviation:** The abbreviation "-NBSGC-" is used extensively throughout the drawing for various materials (wood, angles, furring, etc.). Its meaning is not defined on the sheet.
    *   **Why it matters:** This abbreviation is crucial for understanding material scope, substitutions, or specific project requirements. Without a definition, it can lead to ambiguity regarding which party is responsible for supplying or specifying these items, or what specific material qualities are required.
    *   **Baseline Reference:** Multiple baseline sheets ([#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.9], [#8859 CIBC Int [100] Series FabInstall (1).pdf p.7]) also use this "-NBSGC-" suffix without definition, indicating it's a project-wide convention but still requires clarification for full understanding.

3.  **Ambiguous "Glass Size" Dimensioning:** In details H1 and H2, "GLASS SIZE" is indicated by dimension lines pointing to the glass thickness, but no overall width or height dimensions for the glass panels are provided on this specific detail sheet.
    *   **Why it matters:** While the overall elevations and rough openings are likely dimensioned on other sheets, these detail drawings typically should provide sufficient context for the glass panel dimensions being detailed. This information is crucial for fabrication and understanding the fit within the framed opening.
    *   **Baseline Reference:** Baseline sheets like [#8859 CIBC Int [100] Series FabInstall (1).pdf p.7] also use "GLASS SIZE" with dimension lines that are not numerically quantified on the detail itself, relying on other drawings for full sizing. However, for a detail drawing, it's best practice to at least reference the overall panel dimensions.

4.  **Vague Dimensioning in H1 and H2 (Wood to Glass Gap):** In details H1 and H2, the dimension from the back face of the wood blocking to the front face of the glass is labeled as "1/2"." This measurement encompasses the 7/16" glass and a 1/16" gap. The purpose and exact tolerance of this specific 1/16" gap behind the glass are not explained.
    *   **Why it matters:** This specific gap could relate to sealant application, adhesive tolerance, or thermal considerations. Clarity on its purpose is important for ensuring proper installation and material compatibility.
    *   **Baseline Reference:** Baseline details like [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6] show similar dimension breakdowns but do not always elaborate on the functional purpose of each small increment.

## Items That Match the Standard

*   The general detailing for head (H1) and sill (H2) conditions, including the use of wood blocking, metal angles, and the specified glass thickness, aligns well with standard practices shown in similar baseline details ([#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6]).
*   The use of CRL RTV Silicone for decorative glass is a standard specification.
*   The consistent reference to "SEE ELEVATION FOR TYPE" for glass is a common method for managing design variations across different parts of a project, as seen in similar baseline drawings.
*   The clear labeling of material types such as 7/16" glass, 3/8" painted wood, and the specified metal angles (3"x1"x1/4" Cont. Black Anodized Angle) is consistent with good shop drawing practice.

## Open Questions / Needs Clarification

*   **Definition of "-NBSGC-":** A project-wide definition is needed for the "-NBSGC-" designation.
*   **Specific Type of 7/16" Glass:** The exact specification for the 7/16" glass (beyond "SEE ELEVATION FOR TYPE") for details H1 and H2 needs to be confirmed, likely from other submittal documents referenced by that callout.
*   **Function of 1/16" Gap (H1/H2):** Clarification on the purpose and tolerance of the 1/16" gap between the back of the wood blocking and the glass in H1 and H2 is recommended.
*   **Detail H3 Correction:** The primary need is for the label of Detail H3 to be corrected to reflect its depicted sill condition, or for the detail to be redrawn to accurately represent an elevator head condition.


## Page 7

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7 (0.96), #8859 CIBC Int [100] Series FabInstall (1).pdf p.8 (0.92), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10 (0.91), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8 (0.90), #8859 CIBC Int [100] Series FabInstall (1).pdf p.10 (0.89), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5 (0.89)

## Summary
The design sheet H102 generally aligns with the baseline standard details for similar components. However, several critical dimensions are missing, and some callouts require clarification to ensure proper fabrication and installation.

## Issues Found
1.  **Missing Glass Type Specification:** The design sheet specifies "½" GLASS, SEE ELEVATION FOR TYPE" in details H4, H5, and H6. This defers the crucial glass specification to another sheet.
    *   **Why it Matters:** Glass type (e.g., tempered, laminated, thickness, coatings) is critical for safety, structural integrity, fire ratings, and aesthetic requirements. Without this information on the detail sheet, it's difficult to verify the correct glass is being specified and fabricated.
    *   **Baseline Reference:** Baseline document [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7] also references "See elevation for type" for glass. Baseline document [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8] and [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10] also defer glass type to an elevation. While common to defer to elevations, the lack of specific glass details on the elevation sheet referenced (E102 from [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5]) makes this a point of concern. The elevation sheet E102 only specifies "GL2: 1/2" CLEAR TEMPERED GLASS" for the fixed panels and implies it for the doors, but does not provide details for the "H4/H5/H6" glass callouts which could be different.

2.  **Undefined "-NBSGC-" Callout:** The abbreviation "-NBSGC-" is used extensively for "WOOD BLOCKING", "INTERIOR FINISH", "METAL STUD", and "FINISH FLOOR (TILE)" in details H4, H5, and H6. The meaning of this abbreviation is not defined on the sheet.
    *   **Why it Matters:** This is a critical piece of information required to understand the material properties, manufacturer, or specific requirements for these common components. Without definition, assumptions must be made, potentially leading to incorrect material selection or specification.
    *   **Baseline Reference:** Baseline document [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7] uses "-NBSGC-" identically and without definition. Baseline document [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8] also uses "-NBSGC-" without definition for similar components. Baseline document [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.5] notes "FF-NBSGC: Finished Floor - Not By SGC" which is a partial definition, but doesn't cover other uses.

3.  **Unspecified Dimensions for Door Size, DLO, Frame, and Rough Opening:** Details H4 and H6 show measurement lines and callouts for "DOOR SIZE", "DLO", "WP TO WP / FRAME SIZE", and "ROUGH OPENING" but do not provide numerical values for these critical dimensions.
    *   **Why it Matters:** These dimensions are essential for fabrication and installation to ensure the correct fit of the door and frame within the opening and to confirm clearances for operation and maintenance.
    *   **Baseline Reference:** Baseline document [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7] shows similar callouts for these dimensions but also does not populate them with values, indicating a consistent issue across both the design and baseline sheets. However, the design sheet's lack of these values is still an issue.

4.  **Ambiguous Fastener Spacing Callouts:** In detail H4, the wood blocking is shown spaced at "16" OC". In detail H6, a dimension line associated with the metal stud track has a callout "1 (16" OC)". These are unclear.
    *   **Why it Matters:** While "16" OC" is a standard spacing, the "1" before it in H6 is ambiguous. It might refer to a specific fastener type or quantity, which is not clearly indicated.
    *   **Baseline Reference:** Baseline document [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7] also shows "1 (16" OC)" in detail H6 without clarification of the "1".

5.  **Unclear "WP TO WP / FRAME SIZE" Callout in H6:** The callout "WP TO WP / FRAME SIZE" in detail H6 appears to be truncated or misaligned.
    *   **Why it Matters:** This prevents accurate interpretation of the frame width or related dimensions, impacting fabrication and installation.
    *   **Baseline Reference:** Not directly addressed by baseline comparison, but the lack of clear dimensioning is a general QA concern.

6.  **Unspecified Clad Bottom Rail and Pivot in H5:** Detail H5 describes a "DOOR SILL DETAIL" with "CLAD BOTTOM RAIL & PIVOT" but does not specify the material, finish, or type of the clad bottom rail or the pivot mechanism.
    *   **Why it Matters:** These are critical components for the door's function, durability, and finish. Lack of detail can lead to incorrect selection or performance issues.
    *   **Baseline Reference:** Baseline document [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7] also refers to a "CLAD BOTTOM RAIL & PIVOT" in detail H5 without further specification. Baseline document [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8] details a "CENTER PIVOT" and "ALUMINUM TAPERED BOTTOM RAIL *BRUSHED S.S. CLADDING*", indicating a more complete baseline specification for such elements.

7.  **Unclear Relationship between Closer in H4 and H6:** Detail H4 shows a "CONT. ALUM. HEADER TUBE & RST88 CONCEALED OVERHEAD CLOSER". Detail H6 also specifies a "DOOR HEAD DETAIL W/ CLAD TOP RAIL & HEADER TUBE COC & MAG-LOCK". While "COC" likely refers to Concealed Overhead Closer, the closer itself is not explicitly drawn or called out in the H6 detail section.
    *   **Why it Matters:** It is important to confirm that the closer is accommodated by the header tube and blocking detail in H6, and to understand its specific type and mounting if different from H4.
    *   **Baseline Reference:** Baseline document [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7] lists "COC" for H6 but does not show the closer itself, mirroring the design sheet.

8.  **Redline Comment on Blocking:** A redline comment states: "I THINK WE NEED TO FIX THE BLOCKING SO IT AT LEAST LOOKS LIKE THE FASTENERS ARE GOING INTO IT...".
    *   **Why it Matters:** This indicates a perceived issue with the installation or configuration of the wood blocking, suggesting it may not be properly engaged with fasteners or might be misaligned, which could compromise structural support and the integrity of the connection.
    *   **Baseline Reference:** This is an internal redline on the design sheet itself, not a conflict with a baseline, but it flags a significant constructability issue.

## Items That Match the Standard
*   The general configuration and types of details shown (door head, sill, jamb details) align with common practices for interior glass wall systems as depicted in the baseline reference sheets.
*   The use of standard architectural references (e.g., "ARCH REF: 7/A621") is consistent with the baseline documents.
*   The depiction of metal stud framing, wood blocking, and glass gasket systems are in line with typical assemblies found in the baseline standards.

## Open Questions / Needs Clarification
*   The meaning of the "-NBSGC-" suffix needs to be defined.
*   The exact type, thickness, and specifications of the 1/2" glass for details H4, H5, and H6 need to be provided, either on this sheet or by clear reference to a specific approved glass specification.
*   The dimensions for "DOOR SIZE", "DLO", "WP TO WP / FRAME SIZE", and "ROUGH OPENING" in H4 and H6 need to be populated.
*   The material, finish, and type of the "CLAD BOTTOM RAIL" and "PIVOT" in H5 need to be specified.
*   Clarification is needed on the meaning of "1" in the fastener callout "1 (16" OC)" in detail H6.
*   The redline comment regarding the blocking needs to be addressed and resolved by the contractor and designer.


## Page 8

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8 (0.94), #8859 CIBC Int [100] Series FabInstall (1).pdf p.8 (0.89), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7 (0.89), #8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.5 (0.88), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10 (0.88), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6 (0.88)

## Summary
The design sheet H103 generally aligns with standard detailing practices for interior glass wall systems, particularly in its use of common components and finishes found in the reference drawings. However, several critical details are either missing, ambiguously presented, or differ in a way that requires clarification to ensure proper constructability and performance.

## Issues Found

1.  **Missing Glass Type Specification:** Detail H7 and H8 both specify "1/2" Glass, See Elevation for Type." The glass type is a fundamental specification for performance, safety (e.g., tempered, laminated), and aesthetics. Without this information being present on the detail drawing or a clear reference to where it *is* provided, it's impossible to verify compliance with project requirements.
    *   **Why it matters:** Incorrect glass selection can lead to structural failure, safety hazards, and unintended visual effects.
    *   **Baseline Reference:** All reference drawings ([#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8], [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7], [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.5], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6]) consistently provide glass type information or indicate its absence with a specific reference. For instance, [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8] specifies "1/2" CLEAR TEMPERED GLASS" for detail H7 and "1/2" CLEAR TEMPERED GLASS" for detail H8.

2.  **Undefined "-NBSGC-" Suffix:** The suffix "-NBSGC-" is used repeatedly for "Metal Stud," "Blocking," "Interior Finish," "Finish Floor (Tile)," and "Concrete Floor." The meaning of this abbreviation is not defined on the sheet. While common industry practice may suggest "Not By Salem Glass Company" or similar, this should be explicitly stated or a legend provided for clarity.
    *   **Why it matters:** Ambiguity in material responsibility can lead to misinterpretation during procurement and installation, potentially causing delays or requiring rework.
    *   **Baseline Reference:** While many baseline drawings also use "-NBSGC-" ([#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8], [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6]), the absence of a definition remains an issue of clarity. [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.5] uses the same abbreviation but also fails to define it.

3.  **Ambiguous Fastener Callouts (H8):** In detail H8, fasteners are labeled with "2" and "3" along with "16" OC". The "2" and "3" are not explained and could refer to fastener type, size, or quantity, leading to uncertainty in installation.
    *   **Why it matters:** Incorrect fasteners can compromise structural integrity and the long-term performance of the assembly.
    *   **Baseline Reference:** Baseline drawings often provide more explicit fastener details or legends. For example, [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8] shows fastener callouts but doesn't have similar numerical ambiguities in its sill detail. [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7] shows fastener callouts but they are generally clearer.

4.  **Unclear "WP TO WP" Context:** The term "WP TO WP" (Work Point to Work Point) is used, but its exact reference point and the overall context within the detail are not fully defined. While common, a clearer indication of what these points represent in relation to architectural elements would be beneficial.
    *   **Why it matters:** Inaccurate interpretation of reference points can lead to installation errors and misalignment.
    *   **Baseline Reference:** While "WP TO WP" is common in baseline drawings ([#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8]), its clarity on H103 requires further context. [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.5] explicitly provides dimensions for "WP TO WP" in some instances, demonstrating a more complete presentation.

5.  **Undefined Fastener Materials:** The material and finish for the fasteners are not specified. While typically standard steel, this should be confirmed, especially in areas potentially exposed to moisture or corrosive elements.
    *   **Why it matters:** Inappropriate fastener material can lead to corrosion and potential failure.
    *   **Baseline Reference:** While not always detailed, some baseline drawings specify or imply fastener types more clearly. For example, [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8] shows fasteners but doesn't specify material. [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6] mentions specific fastener types like "Z-Clip and Fastener (TBD-NBSGC)" which is still unclear but more indicative of a required specification.

6.  **Lack of Specific Gasket Material:** The drawings indicate "Black Gasket" but do not specify the material type (e.g., EPDM, Neoprene). This affects the long-term performance and sealing properties.
    *   **Why it matters:** Incorrect gasket material can lead to premature degradation, water and air infiltration.
    *   **Baseline Reference:** Some baseline drawings specify gasket materials more precisely. For instance, [#8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.5] notes "*BLACK RUBBER*" for guides.

## Items That Match the Standard

*   The general layout and use of sectional details (Head and Sill) are consistent with standard practice and the provided baseline drawings ([#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8], [#8859 CIBC Int [100] Series FabInstall (1).pdf p.8], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10], [#8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6]).
*   The use of "Polished S.S Cladding*" for the aluminum tapered rails is consistent with project specifications and reference drawings.
*   The fundamental components shown (metal studs, blocking, interior finish, aluminum rails, glass, gaskets) are standard for this type of system and are reflected in the baseline references.

## Open Questions / Needs Clarification

*   The exact definition and scope of "-NBSGC-" need to be clarified, either by adding a legend to the drawing or by explicit project specification.
*   The specific type and manufacturer of the 1/2" glass must be provided or clearly referenced.
*   The meaning of the numeric labels "2" and "3" associated with fasteners in detail H8 requires clarification.
*   The specific material and finish for all fasteners need to be specified.
*   The specific material for the "Black Gasket" should be identified.
*    A more detailed explanation or diagram for "WP TO WP" reference points would be beneficial for precise installation.


## Page 9

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.9 (0.96), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.6 (0.93), #8859 CIBC Int [100] Series FabInstall (1).pdf p.9 (0.92), #8859 CIBC Int [100] Series FabInstall (1).pdf p.10 (0.89), #8859 CIBC Int [100] Series FabInstall (1).pdf p.7 (0.89), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10 (0.88)

This QA review evaluates the **DESIGN SHEET (V101, Project #8901 Kirkland & Ellis)** against provided **BASELINE** standards for the same project and similar interior glass-wall systems.

## Summary
The sheet generally conforms to the project's established detailing style and material specifications. However, there is a critical contradiction in the General Notes regarding substrate preparation that must be resolved to ensure proper sealant adhesion and aesthetic finish. Existing redline markups on the design sheet correctly identify these areas of concern.

## Issues Found
1. **Contradictory Substrate Note:** The "ARCHITECT/GC NOTE" states the wood should be "**UNPRIMED/PAINTED**." This is logically inconsistent—if wood is unprimed, it is typically unpainted; if it is painted, it requires a primer for most architectural finishes.
    *   **Impact:** Poor adhesion of the CRL RTV Silicone if applied to an incompatible paint/primer, or "read-thru" (ghosting) of the wood grain if the glass back-painting is not 100% opaque.
    *   **Baseline Conflict:** **Baseline #8859 p.9 (CIBC)** provides a much clearer standard: "PLYWOOD SHOULD BE PRIME PAINTED ONLY IN A COLOR... BASED ON THE BACKPAINTED COLOR... TO AVOID READ THRU." The design sheet should be updated to match this logic.
2. **Conflict Between Note and Detail Callouts:** The General Note suggests "UNPRIMED," but the individual details (V1, V2, V3, V4) all specifically call for "**3/8" WOOD PAINTED BLACK**."
    *   **Impact:** Constructability. The GC needs clear instruction on whether to provide raw wood or finished wood. If the silicone is meant to bond to the wood, painting it "Black" introduces a bond-line variable that the glazing contractor (SGC) must approve.
    *   **Baseline Reference:** **Baseline #8901 H101 (p.6)** contains the same error, suggesting a systemic typo in this project's template that needs correction.
3. **Typographical Error in Detail V4:** The redline correctly identifies a correction needed for the word "**DECORATIVE**" in the CRL RTV Silicone callout.
    *   **Impact:** Finish quality/Professionalism.
4. **Fasteners Marked "TBD":** All details show fasteners for the black anodized angles as "TBD PER FIELD CONDITIONS."
    *   **Impact:** Installation delay. While common in early submittals, these must be specified (size, type, spacing) before fabrication to ensure the "NBSGC" (Not By Salem Glass Co.) substrate can support the weight of the 7/16" glass.

## Items That Match the Standard
*   **Material Stack-up:** The use of 7/16" glass with 3/8" wood backing and 1/8" +/- clearances is consistent with **Baseline #8901 H101 (p.6)**.
*   **Scope Delineation:** The use of "-NBSGC-" to clearly define work by others (furring, elevator frames, wood blocking) follows the company standard seen across all baseline sheets.
*   **Hardware Profiles:** The 3" x 1" x 1/4" continuous angles/plates match the project's structural requirements as seen in the H101 head/sill details.

## Open Questions / Needs Clarification
*   **Adhesion Testing:** Has the CRL RTV Silicone been tested for compatibility with the "Black Paint" specified for the wood? If the wood is to be "unprimed," the RTV silicone may soak into the wood fibers, potentially causing failure or staining.
*   **Finish Coordination:** Detail V3 calls for "BLACK ANODIZED" plates and "SS (Stainless Steel)" angles in the same assembly. Please confirm this mixed-metal finish is acceptable to the Architect (HO&K).


## Page 10

**Retrieved baseline matches:** #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.10 (0.97), #8859 CIBC Int [100] Series FabInstall (1).pdf p.10 (0.95), #8859 CIBC Int [100] Series FabInstall (1).pdf p.8 (0.91), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.7 (0.90), #8833 Jones Day ... [100] Int G&G (1st Sub_09.05.25).pdf p.5 (0.89), #8901 Kirkland & Ellis 51st Floor [100] SERIES 1SUB.pdf p.8 (0.89)

This shop-drawing review compares the **Design Sheet (Kirkland & Ellis V102)** against the **Baseline Standards (#8859 CIBC and previous Kirkland & Ellis submittals)**.

## Summary
The design sheet for project #8901 is generally consistent with standard horizontal plan-section details for interior all-glass entrances. However, it lacks architectural cross-references found in similar projects and contains hardware finish callouts that require coordination with the overall interior design intent.

## Issues Found
1.  **Missing Architectural References:** All three details (V5, V6, V7) are labeled "ARCH REF: NONE."
    *   *Why it matters:* This indicates a potential lack of coordination with the architect's contract documents. Baseline Reference #8859 (Sheet V102) provides specific references (e.g., 15/A-8.31 and 16/A-8.31) for these exact conditions to ensure compliance with the design intent.
    *   *Baseline Source:* #8859 CIBC Sheet V102.
2.  **Hardware Finish Ambiguity:** Detail V7 calls for Rockwood RM2510 pulls in "US32/325" (Polished Stainless) and cladding is "POLISHED S.S."
    *   *Why it matters:* Standard office fit-outs (as seen in Baseline #8859) typically utilize "BRUSHED" finishes for maintenance and aesthetics. The reviewer should confirm if the polished finish is a specific design requirement or a clerical carry-over, as polished stainless shows fingerprints more readily in high-traffic door areas.
    *   *Baseline Source:* #8859 CIBC Sheet V102 (Details V5, V6, V7 specify "BRUSHED S.S.").
3.  **Lack of Pivot Detail Clarity:** Detail V6 indicates "PIVOT LOCATION BELOW" with a centerline but does not show the floor-closer or pivot hardware footprint in the plan view.
    *   *Why it matters:* Plan-view details for doors should ideally show the clearance of the pivot hardware to the sidelite rail end-cap to prevent field interference during installation.
    *   *Baseline Source:* Standard practice/Coordination.
4.  **Undefined Acronyms:** The term "-NBSGC-" is used extensively for metal studs, blocking, and finishes.
    *   *Why it matters:* While common (Not By Salem Glass Co.), this acronym is not defined in a legend on this sheet. This can lead to contractual disputes regarding the scope of work for the General Contractor versus the Glazing Subcontractor.
    *   *Baseline Source:* Consistency with #8901 Kirkland & Ellis p.10 description.

## Items That Match the Standard
*   **Gap Clearances:** The 1/8" gaps at the meeting stiles (V7) and door-to-sidelite interface (V6) are industry standard for all-glass systems.
*   **Hardware Dimensions:** The 4" dimension from the glass edge to the centerline of the pulls (V7) matches standard Rockwood installation templates and the CIBC baseline.
*   **Material Thickness:** The use of 1/2" glass is the standard for these unsupported heights in interior office environments.

## Open Questions / Needs Clarification
1.  **Glass Type Specification:** All details note "SEE ELEVATION FOR TYPE." Confirm if glass is tempered or laminated; if laminated, rail prep and adhesive requirements for the polished cladding may change.
2.  **Wall-to-Wall (WP TO WP) Dimensions:** Dimension lines are present in V5, but numerical values are missing. These must be cross-checked against the field-use dimensions or elevations to ensure the glass sizes shown are accurate.
3.  **Anchorage of Bottom Rails:** Detail V5 shows a 3/16" ± clearance but does not show how the bottom rail/track is anchored to the floor or wall. Clarify the fastening method to the metal studs (NBSGC).
