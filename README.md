# Appendix In README FILE

## Ablation Study



### Pearson Correlation with LLM Score (Ablation Study)
This table presents the Pearson correlation coefficients between different feature combinations and the final LLM score, illustrating the contribution of each evaluation dimension to overall scoring alignment.
| Feature Combination     | Pearson Correlation |
|------------------------|---------------------|
| part1 (BLUE)                 | 0.80497             |
| part1(BLEU) + part2(BLEU weight)          | 0.83224             |
|  part1(BLEU) + part2(BLEU weight) + part3 (Blue keyword operator)  | 0.79650             |
|  part1(BLEU) + part2(BLEU weight) + part3 (Blue keyword operator)  + part4 (Similarity string literal)| 0.81388     |
| ELRM                   | 0.81551

<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/ablation_study/pearson.png?raw=true" width="400"/>

Although ELRM yields a slightly lower correlation (0.81551) than the direct combination of `part1 + part2` (0.83224), this does not imply inferior performance. The possible reasons include:

- **ELRM is a reference-aware, weighted metric** that not only considers syntactic alignment but also captures more aspects equivalence, which may reduce its linear correlation with raw LLM scores;
- Unlike simple additive combinations, ELRM tolerates legitimate syntactic variations that preserve functionality, leading to minor deviations from LLM scores in certain edge cases;

In summary, although ELRM has slightly lower correlation, it offers a **more faithful, reference-informed assessment** with better robustness and generalizability across varied generation scenarios.




------------------------------------------------------------------------------------------------------------------------------------------







## CFCEval Framework Dimension Example

### Program Quality
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/GLQ.png?raw=true" width="400"/>


### Fix Capability
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/FC.png?raw=true" width="400"/>


### Post-Transformation Fix Capability
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/PTFC.png?raw=true" width="400"/>

### ELRM

<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/CFCEval_framework_example/ELRM.png?raw=true" width="400"/>



------------------------------------------------------------------------------------------------------------------------------------------

## Leveraged Code Transformation Tyeps with Examples
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/if.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/if2.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/loop.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/Chain.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/order1.png?raw=true" width="400"/>
<img src="https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/code_transformation/order2.png?raw=true" width="400"/>

------------------------------------------------------------------------------------------------------------------------------------------

## GPT-based Metrics (Reference-based Prompts)


### GPT-Tagger (with Copilot results)

#### Program Quality
[查看Program Quality Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/1.txt)
#### Fix Capability
[查看Fix Capability  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/2.txt)
#### Post-Transformation Fix Capability
[查看Post-Transformation Fix Capability Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/3.txt)
#### ELRM
[查看ELRM Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Tagger/4.txt)

------------------------------------------------------------------------------------------------------------------------------------------
### GPT-Scorer (With CodeGeeX results)
#### Program Quality
[查看Program Quality  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/1.txt)
#### Fix Capability
[查看Fix Capability  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/2.txt)
#### Post-Transformation Fix Capability
[查看Post-Transformation Fix Capability  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/3.txt)
#### ELRM
[查看ELRM  Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/GPT-Scorer/4.txt)



------------------------------------------------------------------------------------------------------------------------------------------
### GPT-Tagger (Reference-free Prompts)


#### Post-Transformation Fix Capability
[查看Post-Transformation Fix Capability Prompt](https://github.com/AAAstudyAAA/CFCEval4AIWARE/blob/main/Appendix/reference-free/3.txt)
