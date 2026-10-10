# Source Provenance Ledger — Rheo-Chasmar Drive migration (2026-10-10)

Every document imported from John's Google Drive. Original Drive filenames are preserved
in `docs/sources/original/`. The Drive file ID is the retrieval key for any document
not carried in the repository (binaries and files exceeding the GitHub connector's
per-file write limit are recorded here with checksums and remain retrievable from Drive).

SHA-256 values are of the local copies, which are byte-identical to the Drive downloads
(two files were re-downloaded and checksum-verified; the rest matched by Drive-reported size).

## The six required source documents

| # | Drive file | Drive ID | Repo path | Drive modified | SHA-256 |
|---|---|---|---|---|---|
| 1 | 666-dimensional_math_for_mobile_minds_timestamps.txt | `1-DoVDtB-akOIspTnO7XDwktiq_xbzxHi` | `docs/sources/original/666-dimensional_math_for_mobile_minds_timestamps.txt` | 2026-08-21T01:19:09.428Z | `cf00639bc729fc2e32b5145abd1f2a3832238d315a67280e7e5318da141f3970` |
| 2 | Divergent Hypothesis Dynamics.txt | `181XP3e9Su5c-hbT-I5cL-5CZ4h7sQBFE` | `docs/sources/original/Divergent Hypothesis Dynamics.txt` | 2026-09-17T17:21:57.593Z | `436ce0e77faa4d371651b16dbefd5fea2788b29ebc67b21c6e4a241494abb73d` |
| 3 | Identity_Architecture_Canonical_Technical_Monograph.md | `16JxkJKRST5s-pWNt_00ZQ_dsJ8ZYN520` | `docs/sources/original/Identity_Architecture_Canonical_Technical_Monograph.md` | 2026-08-31T15:08:22.529Z | `8e9baa240b20136c110e7d350e60d7fb6331dd29f7f543efdae880485fef749a` |
| 4 | QMT_qbin_Morphism_Theory_Tier2_Subsystem_Paper_2026-08-31.md | `1WTJXTsdtINbHzXMJyHlpddL_kLsuke5K` | `docs/sources/original/QMT_qbin_Morphism_Theory_Tier2_Subsystem_Paper_2026-08-31.md` | 2026-09-01T04:47:27.581Z | `5ca3265cabc74bd9e067b202ee37cb6edaf713f7a795f1e62deddf44089bd390` |
| 5 | Rheo‑Chasmar Aeon - Cognitive Metamorphic Primer - v3 - current.txt | `14t2ZYRn7Me-A-LfvUEEnk_4gvvCukFGL` | `docs/sources/original/Rheo‑Chasmar Aeon - Cognitive Metamorphic Primer - v3 - current.txt` | 2026-09-03T23:11:52.454Z | `635da80d0dd30112e6257238bd46c52c5b4957680ccec7aa4cff8250fedd49a3` |
| 6 | Transdimensional Memory Substrate.txt | `1orXBlWeTQlGZ0r5PC6uqui0uXk14gsvc` | `docs/sources/original/Transdimensional Memory Substrate.txt` | 2026-10-08T23:22:12.867Z | `c74052521e23fb52e41d39d417a7d576c59355880dea1d2023ae187b8d9e53b8` |

All six were stored in Drive as plain text/markdown (no Google-native export conversion).
Three of the six (Identity monograph, Transdimensional Memory Substrate, QMT paper) are
close to the connector's per-file size limit; they were pushed individually and verified by read-back.

## Imported into `docs/sources/original/` (30 files)

| Drive file | Drive ID | Modified | Size | SHA-256 (truncated) | Notes |
|---|---|---|---|---|---|
| 1024-D Quinary Nexus HSL Reference Geometry - deep research prompt.txt | `1Atuu3Peef6BP4LovpOn-lYdyp3ndeozG` | 2026-09-01T19:21:34.727Z | 20242 | `f85a9a72de82d4d4de39fdaa4fedc426...` | exact-name match |
| 4.4 TMS - Transdimensional Memory Substrate.md | `18L20_cmPOMPDlXlIov_0ILVhclvzcjXL` | 2026-08-31T18:21:18.207Z | 2240 | `8b16c87629e0e5ac59fc6c59b40e3f1b...` | exact-name match |
| 4.9 Worked Example_ Counterfactual Planning with Ephemeral HVDs.md | `1NKOEh2waPCzMSY3SvRLudv8PLSkmRjzT` | 2026-08-31T20:56:18.889Z | 11676 | `09592e8f66ddae6829af53eaab0bb038...` | related .docx variant 1DF84t04wB5Q4J-nA22l7RF7Y_CCmlwcz not retrieved |
| 5. HTLA_ Heterogeneous Labeled State as a Direct Sum.md | `1M9p3TSPojb6ig3RSZ3ti3oGwrU_ITcDT` | 2026-08-31T21:29:00.281Z | 25061 | `f4dd181fd08acc7f98defde12ade278a...` | byte-match (25061) |
| Building_666_Dimensional_Minds_In_Nanobots_timestamps.txt | `1VPxvcXEVp67Of-hZVTgw2QavYTt7wKVN` | 2026-08-21T13:25:16.964Z | 57234 | `79b976e1cef504507ab7b4116e6d8297...` | exact-name match |
| Formal Continuity Without Metaphysical Overreach_ QMT, .qbin Packages, and the Limits of Identity Across Substrate Transformation.md | `10ho4gG7Vn8NUuEKzKXGwG-fvTxVkq7zm` | 2026-09-01T03:43:30.581Z | 38625 | `28760feb7a6739dd30709d48b69d0039...` | byte-match (38625); earlier duplicate 16oQKJzH3crJ2OMV3EmY0vvePaAsXZ0u_ (03:24:40) same bytes; pdf variants exist |
| Formal_Continuity_QMT_qbin_Research_Paper.md | `184xbV18pp7VIXHGwBeEk-8vFPF22jWQZ` | 2026-09-01T02:50:35.559Z | 43874 | `c0bf4fb385dd05c4287ef62b22abface...` | exact-name match |
| HSL Research Blueprint Analysis_.txt | `173O5wZowasDMifL-sc6UWclZeLPsOd-_` | 2026-10-08T23:22:10.780Z | 33764 | `dd35e0ec93671fc850e146e41b43baf0...` | exact-name match |
| HTLA_Mathematical_Paradigm_or_Software_Interface_timestamps.txt | `1kh9kvorT1EnDly7Fy5WtS8XGd1PNsaLC` | 2026-09-01T12:33:42.554Z | 23686 | `a1bccdd3062e2f5f08be4e61d67a1a8b...` | exact-name match |
| HVD_Nexus4_Master_Architecture.md | `1Fhg5bAxMYzcu8RrlDERqfgV09dORvHZV` | 2026-08-26T21:46:37.771Z | 63701 | `8f4f9d11b9b313c8794423a1a444c227...` | exact-name match |
| PDC and other math framework notes - 9-17-2026.txt | `1Y0XWvf5ZH73E081kAkR79EoR5HpLmDKk` | 2026-09-17T16:49:37.024Z | 18017 | `d89c07ff2903c471b1d6d9b9805866e8...` | exact-name match |
| Rheo‑Chasmar Aeon - Cognitive Metamorphic Primer.txt | `1gy4-u6at-jRmGStj6irSb_uUBqU2SCji` | 2026-09-03T18:40:38.304Z | 21054 | `5ccd6796fbac34fda5347b05dab4fd88...` | pre-v1 draft; byte-identical (21054) |
| Rheo‑Chasmar Aeon - Cognitive Metamorphic Primer - v1.txt | `1PaVj38FLhHL9l68pEqoBBXwLSRu4-k3Z` | 2026-09-03T22:44:07.805Z | 25954 | `ce58774f092af544eb067ce9482b9255...` | superseded by v3 |
| Rheo‑Chasmar Aeon - Cognitive Metamorphic Primer - v2.txt | `1GtEMY9C6wYmboE2gX6yvEmVzjhOL71EP` | 2026-09-03T23:01:58.560Z | 42547 | `35d15fbf33c4f407667976701df10b2a...` | superseded by v3 |
| TUCR - UCVM Lesion plus Recovery Experiment Protocol.txt | `14DqfgwESXBRP_WxkwS4WaOerG6QEi_E-` | 2026-08-24T22:53:18.961Z | 3795 | `79fa0fec3cdab7291798909ab44fb100...` | sha256-verified byte-identical; copies at 2026-03-18 (1T3ZKm_7yG_ulClBlOrPufN_Udqldd_RY) and 2026-10-08 (1huHB3n0SqGE5sOycchg0tPRrNpHa3_F, 404 on download - stale listing) |
| The_666_Dimensional_AI_Sparked_by_Music_timestamps.txt | `1PQzvMUUa0ZLJPDq4oGUc3Iqxcrcynmyl` | 2026-08-22T21:22:34.757Z | 42669 | `9e6e61a31a2a0bdc5633d6d4a10fec3c...` | exact-name match |
| dhd deep research prompt - 1.txt | `1OQMjmQdBzrkJxj6-_P3GSEpO87iSNijI` | 2026-09-17T17:00:19.380Z | 37380 | `2e94621a5f82c1d17ff45ce97e9192af...` | exact-name match |
| htla_user_guide.md | `1l_txkBoAegyIlyjF05vdrXAZNFGVbAfy` | 2026-10-08T23:22:13.001Z | 13776 | `6349ba808d1728e759b306e41f12e75b...` | exact-name match |
| nexus4_v2_independent_report - kimi.md | `1dahfBk76IoTj7wqmPvAda_N-peUqHMFi` | 2026-09-03T22:19:56.392Z | 32624 | `cfbb6754d0ddb35d6f75325a08ffdb22...` | exact-name match |
| random notes to remember and implement later.txt | `15kS0WMsrEIR3z1ime1gE1U28TeuqEHnj` | 2026-09-05T05:09:59.188Z | 21918 | `99b9e325d69620641b0e6d6ca7ad5e00...` | exact-name match |
| rheo-chasmar idenity architecture design note - 1.txt | `1jZoDvJ8T_A6N-hm2CtcsFTE-H7wNrTn3` | 2026-09-01T00:00:00.000Z | 12723 | `33b616702328e16655545b8ad71f5c36...` | Drive name misspells 'idenity'; modifiedTime not captured |
| rheo-chasmar integration notes and initial thoughts - 9-17-2026.txt | `1E1II_27NGN7ACbOqDoXrQjOqvJ-9Ue0U` | 2026-09-18T00:45:26.130Z | 9308 | `29857502b2836977fe46741d66cd6f1b...` | exact-name match |
| tucr_conceptual_summary.txt | `1unQr0Gongso3IQXyQOgdRfvOpdYK1baf` | 2026-10-08T23:22:13.003Z | 6897 | `ee9bf3f3bfa7ea0567f601cc9c6b3d70...` | exact-name match |
| tucr_future_research_notes_1.txt | `1phUu9pv01PvQmy9wRE2MeaV9HxNhmVqT` | 2026-10-08T23:22:13.003Z | 316 | `a9638a7c6b5f390b736f93fe055bfe9b...` | exact-name match |

## Recorded here, retained in Drive (18 files)

Not carried as repository files: binaries (PDF/DOCX) cannot be passed through the
GitHub connector's text-based file API, and four text files exceed its ~128KB per-call
argument limit. Each remains retrievable from Drive via its file ID; checksums below
verify any future retrieval.

| Drive file | Drive ID | Modified | Size | SHA-256 (truncated) | Reason |
|---|---|---|---|---|---|
| 1024-D Quinary Nexus HSL Reference Geometry - deep research prompt - answers.txt | `1JdTtRWdQZVbBFW3e4bj3URaIwcedE-gc` | 2026-09-01T20:36:24.191Z | 213313 | `8820c8ebd584eaa4a2006941ff5aed0a...` | exceeds connector per-file write limit |
| Beyond LLMs_ The Radical Architecture of Machines That Never Forget Who They Are.pdf | `16Xco3rYDts1QEAurcTThYYQ8vAyDjpFs` | 2026-09-03T23:19:57.856Z | 97466 | `6b220c6ead29d04d02d2dd13806b831f...` | binary (PDF/DOCX) |
| CA_TUCR_HTLA_First_Mapping_Protocol.pdf | `148K2ubj02c6kWC2ZxPh_NV7QTHxfxDPx` | 2026-08-12T16:41:11.049Z | 121703 | `08dfa619b2d50170fd134081b493d25e...` | binary (PDF/DOCX) |
| Constitutional Amendment Unbounded Resonance and the Slow-Drift Blind Spot - deep research answers.txt | `1duJyniSolyuQ1IqN0NKl_DoQhONF3bEX` | 2026-09-02T20:59:42.905Z | 259382 | `16e8b558e9df41309e97c1fe1a0465c2...` | exceeds connector per-file write limit |
| Deep Research Report_ Divergent Hypothesis Dynamics (DHD) – Round 2.pdf | `1jN8TFKlyuj2fn9HDiMe9_0mIzB0wvYcb` | 2026-09-17T22:41:51.380Z | 83154 | `4c147208beff33bb58ed522c139c818a...` | binary (PDF/DOCX) |
| Divergent_Hypothesis_Dynamics_V1.0.docx | `10bCFD7ygJKj51vFU3KzvD_dS2f4xBB-X` | 2026-09-17T23:08:54.536Z | 388129 | `c9f1f67c1227167e9b935f479a58672d...` | binary (PDF/DOCX) |
| Divergent_Hypothesis_Dynamics_V1.0.pdf | `1q3jbXn7oC_ULXvfNffdvzF64MdPR7bF6` | 2026-09-17T23:09:17.146Z | 573690 | `3cfdbb36522e24a95ea46f4c9a2bc0c7...` | binary (PDF/DOCX) |
| Formal Specification & Implementation Plan for the Hypercontext Salient Lattice (HSL).pdf | `1yYRKmmTx7nK89VhJd3nfIU3ILIdbXizw` | 2026-10-08T23:22:10.590Z | 49353 | `8b9bb5e39132dbdc259f6a653db223c8...` | binary (PDF/DOCX) |
| HARMONIC_SELF-STABILIZING_TRANSDIMENSIONAL_TRAINING_HSTT_and_TUCR_FRAMEWORK.txt | `103UH6NjkGOR9J57LybRmomW1vedCSyFE` | 2026-10-08T23:22:10.636Z | 319164 | `55c5ce07dc2a71cdbcc567a65e3db0ac...` | exceeds connector per-file write limit |
| HTLA_Tier2_Subsystem_Paper_Rewritten_2026-08-31.docx | `1LWF8Bnk_HxDW3kchHOJjpuPqu2l5ur25` | 2026-09-01T00:20:41.137Z | 70169 | `136a9da2b6f19f116ffa1c20871bd5d0...` | binary (PDF/DOCX) |
| HVD 1.5 — Recursive Cognitive Runtime Foundation + TMS Persistence Hardening.pdf | `1Gg_Q7_UUVdjYqi24YuOtAcl8d91OSNB3` | 2026-08-26T22:38:21.599Z | 503822 | `2b1cea2da963c13780e066853553686f...` | binary (PDF/DOCX) |
| HVD Recursive Cognitive Architecture.pdf | `1fz-jIgMZsrgjQqWonPm2QSq4bCOtyM62` | 2026-08-26T22:06:56.541Z | 409220 | `6949a7ba9d5d4f0599b81cf4ad3953d9...` | binary (PDF/DOCX) |
| PROJECT NEXUS — PEANUT GALLERY ARCHITECTURAL REVIEW MEMORANDUM.pdf | `1ROO9uWJSbEbpEn4SN92WlesvI5H0q5Dn` | 2026-08-13T23:26:08.982Z | 879451 | `56201b2f4eeacf3f9271600f38d55f5e...` | binary (PDF/DOCX) |
| QMT_qbin_Morphism_Theory_Tier2_Subsystem_Paper_2026-08-31_REPRODUCED.docx | `15jjoo3Ash5PiNWYkMlySjIHPDJds6BO8` | 2026-09-01T14:56:39.382Z | 77406 | `d060717ced32c545487a9255c00d8402...` | binary (PDF/DOCX) |
| Rheo_Architecture_Primer.pdf | `1xW08xrnVxdE-qu_2rhPdyK1V5IF8jga6` | 2026-09-03T23:25:24.182Z | 19465237 | `c4fc291b96d30dc5e56fcda0c525ebb2...` | binary (PDF/DOCX) |
| Subsystems and Responsibilities of the Rheo-Chasmar Aeon Architecture - Table 1 - v1.pdf | `13H6pc5xw--vzlan98GYekXoijegqc7aA` | 2026-09-03T23:22:47.417Z | 38833 | `553eed6846361a5555862e71f1a10cfe...` | binary (PDF/DOCX) |
| Why 307_ Capacity, Sparsity, Collision, Recoverability, and Structural Vacuum in the 1,024-D Quinary.pdf | `1j9QVOh3yiHL-J3FVj_gJFmzipgARKlV4` | 2026-09-01T19:43:16.805Z | 431688 | `cd538d863bcf7e83b14b20c0c603972f...` | binary (PDF/DOCX) |
| idenity transfer - qmt - deep research responses - 8-31-2026.txt | `1j5vOeOIU6TW1iMCNryLmk4HJZRDzZobb` | 2026-09-01T02:53:44.668Z | 284928 | `93684d2a0bef242b469a5bbf45979d58...` | exceeds connector per-file write limit |

## Version / supersession notes

- **Primer lineage:** undated draft (2026-09-03 18:40) -> v1 (22:44) -> v2 (23:01) -> **v3 current (23:11, authoritative)**.
  The v3 header reads "Formerly Project Nexus 4", confirming the 2026-10-09 rename.
- **TUCR UCVM protocol:** three byte-identical copies (2026-03-18, 2026-08-24, 2026-10-08).
  The 2026-10-08 listing 404s on download (stale listing); the 2026-08-24 copy was checksum-verified.
- **HVD 1.5:** PDF retained in Drive; .md/.docx variants and the superseded `HVD_1_5_ARCHITECTURE.md` (2026-08-25) also in Drive.
- **Peanut Gallery memo:** imported the 2026-08-13 PROJECT NEXUS PDF. A LATER version
  (`Peanut Gallery Architectural Review Memorandum.pdf`, 915019 bytes, 2026-08-14) exists in Drive and is not yet retrieved.
- **DHD:** Round 2 PDF retained in Drive; Round 1 report + .docx variants also in Drive.
- **Formal Continuity / QMT qbin:** the later of two byte-identical .md uploads (2026-09-01 03:43); PDF variants in Drive.
- **Why 307:** PDF retained in Drive; related phonora JSON/timestamps/m4a in Drive.
- Drive filenames `idenity transfer` and `rheo-chasmar idenity architecture design note` preserve the original misspelling of "identity".
- The retrieval agent normalized some filenames on download (underscores/em-dashes -> hyphens);
  the Drive-original names above are authoritative.

## Search coverage

Drive was searched (name + fullText) for: Rheo-Chasmar, Nexus, TUCR, cognitive metamorphic, 666,
qbin, HVD, HTLA, HSL, THDE, HIGC, transdimensional, substrate, Counterfactual Planning, Peanut Gallery,
Why 307, deep research responses, Metamorphic Primer, UCVM Lesion, undated, design note.
Known in Drive but not retrieved: later Peanut Gallery PDF, DHD Round 1, HVD .md/.docx variants,
Beyond LLMs native Google Doc, Formal Continuity PDFs, Why-307 phonora json/txt/m4a, HVD architectural-plan mp4.

