# Course 14 A — Neural Networks and Deep Learning

**Semester VI · 3 credits theory (3 hrs/week) + 1 credit lab (2 hrs/week)**
Syllabus source: pages 1–5 of [the Sem VI PDF](../../../docs/Data-Science-Major-Sem6.pdf)

**This is a Track A course**, paired with
[Course 15 A (Natural Language Processing)](../course-15a-nlp/), and it
continues the track you began in Semester V with Machine Learning and
Artificial Intelligence.

---

## The one thing to understand before anything else

**A neural network is not a new idea bolted onto machine learning. It is the
same idea — fit parameters to minimise a loss — with one change: the features
are learned rather than chosen.**

That single change is the whole course, and it is worth being precise about
what it costs and what it buys.

| Course 12 A taught you | This course changes |
|---|---|
| You engineer features, the model fits weights | **The model engineers its own features** |
| A model with 20 parameters and 1,000 rows | A model with 150,000 parameters and 1,000 rows |
| Overfitting is controlled by model choice | Overfitting is controlled by **dropout, early stopping and data** |
| Training is deterministic and fast | Training is stochastic, slow, and **can fail outright** |
| The model is interpretable if you chose it to be | The model is **not interpretable**, and you must design experiments to find out what it learned |

### 🎯 The single most examinable idea

> **A stack of linear layers is one linear layer.** Without a non-linear
> activation between them, `W₃(W₂(W₁x))` is just `Wx` for `W = W₃W₂W₁`.
> **The activation function is the only reason depth means anything.**

The lab proves it twice: a perceptron cannot learn XOR at all
(`01_perceptron_scratch.py` reports accuracy **0.50**, converged **never**),
and one hidden layer with a non-linearity solves it exactly (**1.00**).

### ⚠️ The mistake this course exists to prevent

> Reporting an accuracy without a baseline. **A deep network that gets 94% on
> a task where a linear model gets 91% has bought you three points for
> 59,210 parameters** — that is the actual measurement from experiment 4, and
> it is the kind of number that should change what you build.

Every experiment here reports a baseline next to the headline number.

---

## What runs here

**Ten of the twelve experiments run against real data and real pre-trained
weights.** That is worth stating plainly, because the usual assumption about
a sandboxed environment is the opposite.

| What the syllabus names | What actually ran |
|---|---|
| MNIST (exp. 4) | **the real MNIST**, a stratified 4,000-image subset |
| Fashion-MNIST (exp. 6, 7) | **the real Fashion-MNIST**, a stratified 8,000-image subset |
| IMDb (exp. 9) | **the real IMDb**, 6,000 training reviews, 10,000-word vocabulary |
| MobileNet, VGG (exp. 8, 11) | **the real published ImageNet networks**, with their real trained weights |
| Keras / TensorFlow | **real Keras 3**, on the torch backend — identical API |

### The two that do not run, and why

| Experiment | Why | Where it lives |
|---|---|---|
| **2** — TensorFlow Playground, Teachable Machine | interactive web apps; there is no output to capture | `02_playground.md` — a full experiment protocol with a results table to fill in |
| **12** — Hugging Face deployment | `huggingface.co` is refused at the gateway with a **403** | `12_huggingface_app.md` — the complete app, the traps, and the error analysis that carries the marks |

Both files carry `*** NOT EXECUTED ***` in their header, and
`tools/run_deeplearning_labs.py` asserts that the marker is still there.

### 📖 Why there are generated datasets as well as real ones

Real data tells you the accuracy. **Only a built dataset can tell you whether
the network learned the thing you intended**, and that check is the difference
between a lab report and a demo.

| Built dataset | The question it can answer that real data cannot |
|---|---|
| XOR, four rows | Did it fail because of *this* limitation, provably? |
| 2,000 review sentences, one decisive word each | Fed that word alone, does the model score it correctly? (**positive 0.9998, negative 0.0002**) |
| Four shapes, a known source→target gap | Did transfer help *because* the features moved, or by luck? |

The lab does both, every time, and says which is which.

---

## The five units

| Unit | Topic | Notes | Hardest part |
|---|---|---|---|
| 1 | Foundations: neurons, perceptrons, activations, loss | [unit-1.md](unit-1.md) | why a stack of linear layers is one linear layer |
| 2 | Training: forward/backward propagation, initialisation, optimisers | [unit-2.md](unit-2.md) | the vanishing gradient, as arithmetic rather than a slogan |
| 3 | CNNs: convolution, pooling, LeNet/AlexNet/VGG | [unit-3.md](unit-3.md) | the output-size formula, and where the parameters actually are |
| 4 | RNNs: sequences, LSTM, GRU, text generation | [unit-4.md](unit-4.md) | why the gates fix what they fix |
| 5 | Advanced: transfer learning, attention, transformers, ethics | [unit-5.md](unit-5.md) | attention as a weighted average you can compute by hand |

Plus [lab.md](lab.md) — all twelve experiments with their measured output —
and [practice.md](practice.md) — exam questions with worked solutions.

---

## How this course connects to the rest of the programme

| Course | What it gives you here |
|---|---|
| **Course 3** (Python) | NumPy array thinking; every layer is a matrix multiply |
| **Course 4** (Statistics) | loss functions are likelihoods; cross-entropy is one |
| **Course 9** (Python for Data Analysis) | the train/test discipline this course depends on |
| **Course 12 A** (Machine Learning) | the baselines. **Do not skip them** |
| **Course 13 A** (AI) | search and optimisation; gradient descent is one more optimiser |
| **Course 15 A** (NLP) | takes the RNN and attention material and applies it to language |

---

## If you read one thing

**Unit 2**, and specifically the part on what makes training fail. Depth,
width and architecture are choices you can reason about. A learning rate that
is 100× too large produces a model that never learns anything, and the
experiment 4 table shows exactly that — **`lr=10.0` finished at accuracy
0.1000 with the loss having gone *up*.**

Nothing else in the course matters if training does not converge.
