The pipeline for each paper
Prerequisites (before reading). If you can't follow the paper, don't push through it. Find the one concept you're missing (backprop, softmax and cross-entropy, convolutions, gradients) and revise only that.
Pass 1 (15 min): abstract, figures, conclusion. Write down what problem it solves.
Pass 2 (1 to 2 hours): full read. Skip proofs on the first go. Write down every term you don't understand.
Close the paper and explain it in 5 lines from memory: problem, key idea, how it works, results, limitations. If you can't, you haven't understood it, so reread.
Code the core idea only. Build the one thing the paper introduced (the residual block, the dropout layer), not the whole system.
Run an experiment. Compare with and without the idea (plain net vs ResNet, with vs without dropout), and record the numbers.
Write it up in the repo's README for that paper: summary, code, results, and what surprised you.
Build something with it (for the hard papers; the easy ones don't need this): apply the idea to a small real problem, like using ResNet on your own dataset or a Seq2Seq model for a small task.