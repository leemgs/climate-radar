# Robustness analyses (second round)

- First period only (between-subjects, no carry-over): AER 0.825 (n=28) vs 0.642 (n=24), diff +0.183 [0.079, 0.287], Welch t(40.9) = 3.56, p = 0.00096, d = 1.02; Mann-Whitney p = 0.00098.
- First period only, latency: 8.09 vs 12.28 s, diff -4.19 [-4.60, -3.78], t = -20.57, p = 9.3e-25, d = -5.79.
- GEE adjusted for reference action and order: OR = 2.61 [1.97, 3.46], p = 2.2e-11.
- AI minus baseline AER within each reference action: Issue_Alert +0.07, Monitor +0.26, Recommend_Evacuation +0.22, Shelter_in_Place +0.20, Standby +0.19; AI AER standardized to the baseline mix: 0.814.
- Participants with higher AER under AI: 42/52 (equal 5, lower 5); sign test p = 2.5e-08; paired permutation p < 5e-5 (20,000 sign flips).
- Dropping the 3 most extreme participants: mean diff +0.169, t = 6.49, p = 4.5e-08.
