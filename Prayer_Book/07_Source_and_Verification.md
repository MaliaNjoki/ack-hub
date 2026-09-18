# Prayer Book Source and Verification

## 1. Purpose

This file establishes the source, verification, evidence, copyright, and data-quality rules for the ACK Hub `Prayer_Book/` collection.

Its purpose is to prevent unsupported claims, invented liturgical wording, incorrect publication relationships, and confusion between historical and current ACK resources.

---

## 2. Primary Source Authority

For ACK-specific prayer-book information, the preferred source hierarchy is:

### Level 1 — Official ACK Sources

These include:

* official Anglican Church of Kenya websites;
* official ACK publications;
* official ACK institutional pages;
* official provincial documents;
* official diocesan documents where the information is diocesan-specific.

These sources have the highest priority for ACK-specific claims.

---

### Level 2 — ACK Uzima Publishing House

ACK Uzima Publishing House is particularly important for:

* prayer books;
* liturgical publications;
* hymn books;
* Church Lectionary and Diary;
* publication history;
* language editions;
* related Christian literature.

For publication-level information, Uzima should be treated as a primary ACK source.

---

### Level 3 — Official ACK Publications

Examples include:

* ACK strategic documents;
* provincial reports;
* official church publications;
* authorised educational and liturgical documents.

These are particularly useful for historical development and institutional context.

---

### Level 4 — Authoritative Bibliographic Sources

These may include:

* university library catalogues;
* national library catalogues;
* established bibliographic databases;
* WorldCat and comparable authoritative catalogues.

These sources can help verify:

* title;
* author/editor;
* publisher;
* publication year;
* edition;
* pagination;
* ISBN or catalogue information where available.

They should not automatically be treated as proof of current ACK authorisation.

---

### Level 5 — Reliable Secondary Sources

Secondary sources may be used for supporting context.

They should be clearly distinguished from official ACK information.

---

### Level 6 — Unverified Online Material

Unsourced websites, social-media posts, user uploads and unattributed documents should not be treated as authoritative evidence for ACK prayer-book claims.

They may identify leads for further research but should not establish facts on their own.

---

## 3. Evidence Labels

ACK Hub should use the following evidence labels.

### VERIFIED — ACK

The information is directly supported by an official ACK source.

### VERIFIED — UZIMA

The information is directly supported by ACK Uzima Publishing House.

### VERIFIED — PUBLICATION

The information is supported by an official ACK publication.

### VERIFIED — CATALOGUE

The information is supported by a reliable bibliographic or library catalogue.

### CONTEXT — ANGLICAN

The information describes wider Anglican or historical Anglican practice and must not be presented as uniquely ACK-specific.

### HISTORICAL — ACK

The information is verified as part of ACK's historical development but should not automatically be treated as current.

### PLACEHOLDER — VERIFY

The information has not yet been sufficiently verified and must not be presented as established fact.

---

## 4. Current vs Historical Information

A publication's historical existence does not automatically establish its current status.

ACK Hub should distinguish:

* publication history;
* historical editions;
* current editions;
* current availability;
* current authorisation;
* discontinued or superseded resources.

For example, the fact that a resource appears in an older Uzima catalogue should not by itself establish that the same edition is currently available or currently authorised.

Current-status claims require a current authoritative source.

---

## 5. Edition Verification

Where an edition is relevant, verify as many of the following as possible:

* exact title;
* subtitle;
* publisher;
* edition number;
* publication year;
* revision year;
* language;
* pagination;
* ISBN;
* catalogue record;
* official ACK status;
* availability.

If some details cannot be verified, mark them:

**PLACEHOLDER — VERIFY**

Do not fill missing bibliographic information by inference.

---

## 6. Language Verification

Language claims must be tied to the specific resource.

For example:

**Verified:**

*Kitabu Kipya Cha Ibaada* — Kiswahili translation of *Our Modern Services*.

**Verified:**

ACK Uzima identifies *Modern English Services* as a modern-English rendering of services from the 1662 Book of Common Prayer.

**Verified:**

ACK Uzima identifies English, Kiswahili and Kikuyu material in connection with the Mothers' Union Prayer Book.

Do not assume that because one ACK resource exists in a particular language, every ACK liturgical resource exists in that language.

---

## 7. Publication Relationships

When two resources are related, ACK Hub should document the relationship explicitly.

Current verified relationships include:

```text
Our Modern Services
        │
        └── Kitabu Kipya Cha Ibaada
            Kiswahili translation
                    │
                    └── Kiswahili Prayer Book
                        Abridged version
```

A separate relationship exists for:

```text
1662 Book of Common Prayer
        │
        └── Modern English Services
            Modern-English rendering of services
```

These relationships should not be interpreted as evidence that the resources are interchangeable.

---

## 8. Service-Level Verification

A service category should not automatically be treated as an exact component of a particular publication.

For example, the existence of:

* baptism;
* confirmation;
* marriage;
* funeral;
* ordination;
* Holy Communion;
* morning prayer;

within the ACK liturgical tradition does not, by itself, establish that a particular edition of a prayer book contains that exact service.

Edition-specific claims require edition-level verification.

---

## 9. Exact Text Verification

Exact prayer or service wording should only be provided when:

1. the source is authoritative or appropriately licensed;
2. the exact edition is known;
3. the wording has been verified against that source;
4. reproduction is legally permitted.

If the exact text cannot be verified, ACK Hub should say so rather than reconstructing or guessing the wording.

---

## 10. Copyright Protection

Prayer books and liturgical publications may contain copyrighted material.

ACK Hub should not reproduce substantial portions of copyrighted:

* prayers;
* liturgies;
* Eucharistic services;
* baptismal services;
* marriage services;
* funeral services;
* ordination services;
* rubrics;
* congregational responses;
* hymn texts;
* copyrighted translations.

The repository should prioritise:

* metadata;
* summaries;
* service categories;
* historical context;
* source references;
* verification information;
* retrieval instructions.

---

## 11. Source Conflict Rules

When two sources provide conflicting information:

### Step 1

Identify the exact claim that conflicts.

### Step 2

Check whether one source is newer.

### Step 3

Check whether one source has higher institutional authority.

### Step 4

Determine whether the difference represents:

* a new edition;
* a historical change;
* a language difference;
* a diocesan variation;
* a catalogue error;
* incomplete information.

### Step 5

Record the discrepancy where necessary.

Do not silently select a preferred answer when the evidence remains uncertain.

---

## 12. Current Practice Rule

For statements such as:

* "ACK currently uses..."
* "This is the current prayer book..."
* "This is the authorised edition..."
* "All ACK churches use..."
* "This service is mandatory..."

the assistant must have current authoritative evidence.

Historical evidence alone is insufficient.

---

## 13. Provincial, Diocesan and Parish Scope

ACK operates through different levels of church organisation.

Information should therefore be tagged according to scope:

### Provincial

Applies to the Province of Kenya.

### Diocesan

Applies to a particular ACK diocese.

### Parish / Local

Applies to a particular parish or local congregation.

### Historical

Applies to a defined historical period.

### General Anglican

Wider Anglican context that is not necessarily ACK-specific.

A local practice must never automatically be generalised to the whole Province.

---

## 14. Retrieval Rules for ACK Hub

When a user asks a prayer-book question, the assistant should follow this sequence:

1. Identify the resource.
2. Identify the language.
3. Identify the edition where relevant.
4. Determine whether the question concerns current or historical information.
5. Determine the geographical/ecclesial scope.
6. Retrieve the highest-authority source available.
7. Verify the claim.
8. Distinguish fact from Anglican context.
9. Respect copyright.
10. Provide a concise answer with the appropriate source reference.

---

## 15. Resource-Specific Verification

### Our Modern Services

Verified:

* ACK liturgical resource;
* adopted by the Province of Kenya in 2002;
* published through ACK Uzima;
* language editions/services identified by Uzima.

See:

`01_Our_Modern_Services.md`

---

### Kitabu Kipya Cha Ibaada

Verified:

* Kiswahili resource;
* identified by Uzima as the Swahili translation of *Our Modern Services*.

See:

`02_Kitabu_Kipya_Cha_Ibaada.md`

---

### Kiswahili Prayer Book

Verified:

* Kiswahili resource;
* identified by Uzima as an abridged version of *Kitabu Kipya Cha Ibaada*.

See:

`03_Kiswahili_Prayer_Book.md`

---

### Modern English Services

Verified:

* modern-English liturgical resource;
* identified by Uzima as services from the 1662 Book of Common Prayer rendered in modern English.

See:

`04_Modern_English_Services.md`

---

### Mothers' Union Prayer Book

Verified:

* separate Mothers' Union prayer resource;
* associated language material identified by Uzima includes English, Kiswahili and Kikuyu;
* catalogue description includes prayer and supplication material.

See:

`05_Mothers_Union_Prayer_Book.md`

---

## 16. Source Recording

Every factual resource entry should record enough information to identify its source.

Where practical, record:

* source institution;
* source title;
* publication/page title;
* publication date;
* URL or repository location;
* access/verification date;
* evidence label.

For online sources, the date of verification is important because websites and catalogues can change.

---

## 17. Verification Date

The current Prayer Book collection was initially verified in:

**September 2026**

Future changes should update the verification date when new authoritative information is incorporated.

---

## 18. AI Safety and Accuracy Rules

ACK Hub must never:

* invent a prayer;
* invent a liturgical response;
* fabricate a table of contents;
* assume an edition's contents;
* present general Anglican practice as ACK policy;
* treat historical information as current without verification;
* treat a diocesan practice as provincial;
* merge distinct prayer books;
* claim current authorisation without current evidence.

When evidence is insufficient, the correct response is:

**"This requires verification from the authorised ACK resource."**

---

## 19. Related Sources and Files

### Prayer Book

* `README.md`
* `01_Our_Modern_Services.md`
* `02_Kitabu_Kipya_Cha_Ibaada.md`
* `03_Kiswahili_Prayer_Book.md`
* `04_Modern_English_Services.md`
* `05_Mothers_Union_Prayer_Book.md`
* `06_Liturgical_Resources.md`

### Liturgy

`../Liturgy/`

### Church Calendar

`../Liturgical_Seasons_and_Colours.md`

### Constitution

`../constitution.md`

---

## Data Quality Rule

**Evidence before assertion.**

Every ACK-specific prayer-book claim should be:

* sourced;
* scope-identified;
* date-aware;
* edition-aware where necessary;
* clearly separated from general Anglican context;
* labelled when uncertain.

**Last verification:** September 2026.
