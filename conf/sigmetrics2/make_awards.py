#!/usr/bin/env python3
"""
make_awards.py — write data/awards.json from the SIGMETRICS awards page
(https://www.sigmetrics.org/awards.shtml). Static transcribed data; the website overlays
it onto sigmetrics.json by matching paper TITLES and author NAMES — no DBLP refetch needed.
Edit the lists below when the awards page adds new entries.
"""
import json, os, time

# ---- author awards: {year, name} ----
ACHIEVEMENT = [
    (2026,"Alexandre Proutiere"),(2025,"Devavrat Shah"),(2024,"Marco Ajmone Marsan"),
    (2023,"Laurent Massoulié"),(2022,"Balaji Prabhakar"),(2021,"R. Srikant"),
    (2020,"Leandros Tassiulas"),(2019,"Mary Vernon"),(2018,"Jim Dai"),(2017,"Sem Borst"),
    (2016,"John Tsitsiklis"),(2015,"Bruce Hajek"),(2014,"François Baccelli"),
    (2013,"Jean Walrand"),(2012,"Debasis Mitra"),(2011,"Onno J. Boxma"),
    (2010,"Jeffrey P. Buzen"),(2009,"Frank Kelly"),(2008,"Erol Gelenbe"),
    (2007,"Don F. Towsley"),(2006,"Richard R. Muntz"),(2005,"Stephen S. Lavenberg"),
    (2004,"Ken C. Sevcik"),(2003,"Ed G. Coffman"),
]
RISING_STAR = [
    (2026,"Sangeetha Abdu Jyothi"),(2025,"Debankur Mukherjee"),(2024,"Christina Lee Yu"),
    (2023,"Weina Wang"),(2022,"Giulia Fanti"),(2021,"Zhenhua Liu"),(2020,"Kuang Xu"),
    (2019,"Anshul Gandhi"),(2018,"Longbo Huang"),(2017,"Sewoong Oh"),(2016,"Yi Lu"),
    (2015,"Jinwoo Shin"),(2014,"Florian Simatos"),(2013,"Augustin Chaintreau"),
    (2012,"Marc Lelarge"),(2011,"Adam Wierman"),(2010,"Milan Vojnovic"),
    (2009,"Alexandre Proutiere"),(2008,"Devavrat Shah"),
]

# ---- test of time: {awardYear, paperYear, title, authors[]} ----
TEST_OF_TIME = [
    (2026,2016,"On the Approximation Error of Mean-Field Models",["Lei Ying"]),
    (2025,2015,"Learning to Rank: Regret Lower Bounds and Efficient Algorithms",["Richard Combes","Stefan Magureanu","Alexandre Proutiere","Cyrille Laroche"]),
    (2024,2014,"A Measurement Study of Google Play",["Nicolas Viennot","Edward Garcia","Jason Nieh"]),
    (2023,2013,"Root Cause Detection in a Service-Oriented Architecture",["Myunghwan Kim","Roshan Sumbaly","Sam Shah"]),
    (2022,2012,"Workload Analysis of a Large-Scale Key-Value Store",["Berk Atikoglu","Yuehai Xu","Eitan Frachtenberg","Song Jiang","Mike Paleczny"]),
    (2021,2011,"Greening Geographical Load Balancing",["Zhenhua Liu","Minghong Lin","Adam Wierman","Steven Low","Lachlan L.H. Andrew"]),
    (2020,2010,"Detecting Sources of Computer Viruses in Networks: Theory and Experiment",["Devavrat Shah","Tauhid Zaman"]),
    (2019,2009,"Network adiabatic theorem: an efficient randomized protocol for contention resolution",["Shreevatsa Rajagopalan","Devavrat Shah","Jinwoo Shin"]),
    (2018,2008,"Counter braids: a novel counter architecture for per-flow measurement",["Yi Lu","Andrea Montanari","Balaji Prabhakar","Sarang Dharmapurikar","Abdul Kabbani"]),
    (2017,2007,"An analysis of latent sector errors in disk drives",["Lakshmi N. Bairavasundaram","Garth R. Goodson","Shankar Pasupathy","Jiri Schindler"]),
    (2016,2005,"An analytical model for multi-tier internet services and its applications",["Bhuvan Urgaonkar","Giovanni Pacifici","Prashant Shenoy","Mike Spreitzer","Asser Tantawi"]),
    (2015,2005,"Internet Traffic Classification Using Bayesian Analysis Techniques",["Andrew W. Moore","Denis Zuev"]),
    (2014,2004,"Myths and Realities: the Performance Impact of Garbage Collection",["Stephen Blackburn","Perry Cheng","Kathryn McKinley"]),
    (2013,2003,"Fast Accurate Computation of Large-Scale IP Traffic Matrices from Link Loads",["Yin Zhang","Matthew Roughan","Nick Duffield","Albert Greenberg"]),
    (2012,2002,"Network Tomography on General Topologies",["Tian Bu","Nick Duffield","Francesco Lo Presti","Don Towsley"]),
    (2011,2000,"A Case for End System Multicast",["Yang-hua Chu","Sanjay Rao","Hui Zhang"]),
    (2011,2000,"Stable Internet Routing without Global Coordination",["Lixin Gao","Jennifer Rexford"]),
    (2010,1976,"Fundamental Laws of Computer System Performance",["Jeffrey P. Buzen"]),
    (2010,1985,"A Comparison of Receiver-initiated and Sender-initiated Adaptive Load Sharing",["Derek Eager","Ed Lazowska","John Zahorjan"]),
    (2010,1996,"Self-similarity in World Wide Web Traffic: Evidence and Possible Causes",["Mark E. Crovella","Azer Bestavros"]),
]

# ---- best paper / student / runner-up: {year, title, authors[], type} ; type in best|student|both|runner ----
PAPER_AWARDS = [
    (2026,"Sequential Fair Allocation With Replenishments: A Little Envy Goes An Exponentially Long Way",["Chido Onyeze","Sean R. Sinclair","Chamsi Hssaine","Siddhartha Banerjee"],"best"),
    (2026,"Wasserstein-p Central Limit Theorem Rates: From Local Dependence to Markov Chains",["Yixuan Zhang","Qiaomin Xie"],"student"),
    (2026,"From Measurement to Emissions: Assessing the Carbon Footprint of Traffic Flows",["Sawsan El-Zahr","Noa Zilberman"],"runner"),
    (2026,"Shedding Light on Shadows: Automatically Tracing Illicit Money Flows on EVM-Compatible Blockchains",["Yicheng Huo","Yufeng Hu","Yajin Zhou","Ting Yu","Lei Wu","Cong Wang"],"runner"),
    (2026,"A Minimal-Assumption Analysis of Q-Learning with Time-Varying Policies",["Phalguni Nanda","Zaiwei Chen"],"runner"),
    (2025,"Adversarial Network Optimization under Bandit Feedback: Maximizing Utility in Non-Stationary Multi-Hop Networks",["Yan Dai","Longbo Huang"],"best"),
    (2025,"Beaver: A High-Performance and Crash-Consistent File System Cache via PM-DRAM Collaborative Memory Tiering",["Qinglin Pan","Ji Qi","Jiatai He","Heng Zhang","Jiageng Yu","Yanjun Wu"],"student"),
    (2025,"Combinatorial Logistic Bandits",["Xutong Liu","Xiangxiang Dai","Xuchuang Wang","Mohammad Hajiesmaili","John C.S. Lui"],"runner"),
    (2025,"On the Distribution of Sojourn Times in Tandem Queues",["Florin Ciucu","Sima Mehri"],"runner"),
    (2025,"Game Theoretic Liquidity Provisioning in Concentrated Liquidity Market Makers",["Weizhao Tang","Rachid Elazouzi","Cheng Han Lee","Ethan Chan","Giulia Fanti"],"runner"),
    (2024,"Agents of Autonomy: A Systematic Study of Robotics on Modern Hardware",["Mohammad Bakhshalipour","Phillip B. Gibbons"],"best"),
    (2024,"Strongly Tail-Optimal Scheduling in the Light-Tailed M/G/1",["George Yu","Ziv Scully"],"best"),
    (2024,"Fair Resource Allocation in Virtualized O-RAN Platforms",["Fatih Aslan","George Iosifidis","Jose A. Ayala-Romero","Andres Garcia-Saavedra","Xavier Costa-Perez"],"student"),
    (2024,"CarbonScaler: Leveraging Cloud Workload Elasticity for Optimizing Carbon-Efficiency",["Walid A. Hanafy","Qianlin Liang","Noman Bashir","David Irwin","Prashant Shenoy"],"student"),
    (2023,"Mean-field Analysis for Load Balancing on Spatial Graphs",["Daan Rutten","Debankur Mukherjee"],"best"),
    (2023,"Overcoming the Long Horizon Barrier for Sample-Efficient Reinforcement Learning with Latent Low-Rank Structure",["Tyler Sam","Yudong Chen","Christina Lee Yu"],"student"),
    (2022,"WISEFUSE: Workload Characterization and DAG Transformation for Serverless Workflows",["Ashraf Mahgoub","Edgardo Barsallo Yi","Karthick Shankar","Eshaan Minocha","Somali Chaterji","Sameh Elnikety","Saurabh Bagchi"],"best"),
    (2022,"Offline and Online Algorithms for SSD Management",["Tomer Lange","Joseph (Seffi) Naor","Gala Yadgar"],"student"),
    (2021,"Nudge: Stochastically Improving upon FCFS",["Isaac Grosof","Kunhe Yang","Ziv Scully","Mor Harchol-Balter"],"best"),
    (2021,"A Look Behind the Curtain: Traffic Classification in an Increasingly Encrypted Web",["Iman Akbari","Mohammad A. Salahuddin","Shi-Han Wen","Noura Limam","Raouf Boutaba","Bertrand Mathieu","Stephanie Moteau","Stephane Tuffin"],"student"),
    (2020,"Rateless Codes for Near-Perfect Load Balancing in Distributed Matrix-Vector Multiplication",["Ankur Mallick","Malhar Chaudhari","Utsav Sheth","Ganesh Palanikumar","Gauri Joshi"],"best"),
    (2020,"Optimal Data Placement for Heterogeneous Cache, Memory, and Storage Systems",["Lei Zhang","Reza Karimi","Irfan Ahmad","Ymir Vigfusson"],"student"),
    (2019,"Computationally Efficient Estimation of the Spectral Gap of a Markov Chain",["Richard Combes","Mikael Touati"],"best"),
    (2019,"Load Balancing Guardrails: Keeping Your Heavy Traffic on the Road to Low Response Times",["Isaac Grosof","Ziv Scully","Mor Harchol-Balter"],"student"),
    (2018,"A refined mean field approximation",["Nicolas Gast","Benny van Houdt"],"best"),
    (2017,"Accelerating Performance Inference over Closed Systems by Asymptotic Methods",["Giuliano Casale"],"best"),
    (2017,"Security Game with Non-additive Utilities and Multiple Attacker Resources",["Sinong Wang","Ness Shroff"],"student"),
    (2016,"On the Duration and Intensity of Competitions in Nonlinear Pólya Urn Processes with Fitness",["Bo Jiang","Daniel R. Figueiredo","Bruno Ribeiro","Don Towsley"],"best"),
    (2016,"The Value of Privacy: Strategic Data Subjects, Incentive Mechanisms and Fundamental Limits",["Weina Wang","Lei Ying","Junshan Zhang"],"student"),
    (2015,"Spy vs. Spy: Rumor Source Obfuscation",["Giulia Fanti","Peter Kairouz","Sewoong Oh","Pramod Viswanath"],"best"),
    (2015,"Fisher Information-based Experiment Design for Network Tomography",["Ting He","Chang Liu","Ananthram Swami","Don Towsley","Theodoros Salonidis","Andrei Iu. Bejan","Paul Yu"],"student"),
    (2014,"Concave switching in single and multihop networks",["Neil Walton"],"best"),
    (2014,"A Measurement Study of Google Play",["Nicolas Viennot","Edward Garcia","Jason Nieh"],"student"),
    (2013,"Queueing System Topologies with Limited Flexibility",["John N. Tsitsiklis","Kuang Xu"],"both"),
    (2012,"Temperature Management in Data Centers: Why Some (Might) Like It Hot",["Nosayba El-Sayed","Ioan Stefanovici","George Amvrosiadis","Andy A. Hwang","Bianca Schroeder"],"best"),
    (2012,"Optimal Queue-Size Scaling in Switched Networks",["Devavrat Shah","Neil Walton","Yuan Zhong"],"student"),
    (2011,"Topology Discovery of Sparse Random Graphs with Few Participants",["Animashree Anandkumar","Avinatan Hassidim","Jonathan Kelner"],"best"),
    (2011,"Network Architecture for Joint Failure Recovery and Traffic Engineering",["Martin Suchara","Dahai Xu","Robert Doverspike","David Johnson","Jennifer Rexford"],"student"),
    (2010,"Load Balancing via Randomized Local Search in Closed and Open Systems",["Ayalvadi Ganesh","Sarah Lilienthal","D. Manjunath","Alexandre Proutiere","Florian Simatos"],"best"),
    (2010,"Distributed Sensor Network Localization from Local Connectivity: Performance Analysis for the HOP-TERRAIN Algorithm",["Amin Karbasi","Sewoong Oh"],"student"),
    (2009,"The Age of Gossip: Spatial Mean Field Regime",["Augustin Chaintreau","Jean-Yves Le Boudec","Nikodin Ristanovic"],"best"),
    (2009,"Network adiabatic theorem: An efficient randomized protocol for contention resolution",["Shreevatsa Rajagopalan","Devavrat Shah","Jinwoo Shin"],"student"),
    (2008,"Counter Braids: A Novel Counter Architecture for Per-Flow Measurement",["Yi Lu","Andrea Montanari","Balaji Prabhakar","Sarang Dharmapurikar","Abdul Kabbani"],"best"),
    (2008,"Fully Decentralized Emulation of Best-Effort and Processor Sharing Queues",["Rade Stanojevic","Robert Shorten"],"student"),
    (2007,"Modeling the relative fitness of storage",["Michael Mesnier","Matthew Wachs","Raja R. Sambasivan","Alice Zheng","Gregory R. Ganger"],"best"),
    (2007,"An Analysis of Latent Sector Errors in Disk Drives",["Lakshmi Bairavasundaram","Garth Goodson","Shankar Pasupathy","Jiri Schindler"],"student"),
    (2006,"Maximizing Throughput in Wireless Networks via Gossiping",["Eytan Modiano","Devavrat Shah","Gil Zussman"],"best"),
    (2006,"GPS Scheduling: Selection of Optimal Weights and Comparison with Strict Priorities",["Pascal Lieshout","Michel R.H. Mandjes","Sem Borst"],"student"),
    (2005,"Coupon Replication Systems",["Laurent Massoulié","Milan Vojnović"],"best"),
    (2005,"A Network Service Curve Approach for the Stochastic Analysis of Networks",["Florin Ciucu","Almut Burchard","Jorg Liebeherr"],"student"),
    (2004,"On performance bounds for the integration of elastic and adaptive streaming flows",["Thomas Bonald","Alexandre Proutière"],"best"),
    (2003,"Classifying Scheduling Policies with respect to Unfairness in an M/GI/1",["Adam Wierman","Mor Harchol-Balter"],"student"),
    (2002,"PC Based Precision Timing Without GPS",["Attila Pásztor","Darryl Veitch"],"student"),
    (1996,"Exploiting Process Lifetime Distributions for Dynamic Load Balancing",["Mor Harchol-Balter","Allen Downey"],"best"),
    (1996,"Supporting stored video: reducing rate variability and end-to-end resource requirements through optimal smoothing",["James D. Salehi","Zhi-Li Zhang","James F. Kurose","Don Towsley"],"best"),
]

# ---- doctoral dissertation award: {year, kind, name, institution, advisor, title} ----
DOCTORAL = [
    (2025,"winner","Weizhao Tang","Carnegie Mellon University","Giulia Fanti","Algorithmic Techniques for Utility Improvement across the Blockchain Stack"),
    (2025,"honorable","Vamsi Addanki","Technische Universität Berlin","Stefan Schmid","Adaptive Protocols and Reconfigurable Optical Interconnects for Datacenter Networks"),
    (2025,"honorable","Pengfei Li","University of California, Riverside","Shaolei Ren","Learning-Augmented Online Decision Making: Algorithms, Analysis, and Applications"),
    (2024,"winner","Sushil Varma","Georgia Tech","Siva Theja Maguluri","Stochastic Matching Networks: Theory and applications to matching platforms"),
    (2024,"honorable","Diego Goldsztajn","Eindhoven University of Technology","Sem Borst; Johan van Leeuwaarden","Fluid limits and optimal task assignment policies for locally pooled service systems"),
    (2024,"honorable","Ayush Mishra","National University of Singapore","Ben Leong","Understanding the Modern Internet’s Heterogeneous Congestion Control Landscape"),
    (2023,"winner","Isaac Grosof","Carnegie Mellon University","Mor Harchol-Balter","Optimal Scheduling in Multiserver Queues"),
    (2023,"honorable","Prakirt Raj Jhunjhunwala","Georgia Institute of Technology","Siva Theja Maguluri","Design and Analysis of Stochastic Processing and Matching Networks"),
    (2023,"honorable","Sean Sinclair","Cornell University","Christina Lee Yu; Siddartha Banerjee","Adaptivity, Structure, and Objectives in Sequential Decision-Making"),
    (2022,"winner","Ziv Scully","Carnegie Mellon University","Mor Harchol-Balter","A New Toolbox for Scheduling Theory"),
    (2022,"honorable","Anish Agarwal","Massachusetts Institute of Technology","Alberto Abadie; Munther Dahleh; Devavrat Shah","Causal Inference for Social and Engineering Systems"),
    (2022,"honorable","Zaiwei Chen","Georgia Institute of Technology","Siva Theja Maguluri; John Paul Clarke","A Unified Lyapunov Framework for Finite-Sample Analysis of Reinforcement Learning Algorithms"),
]

out = {
    "generatedAt": int(time.time()*1000),
    "source": "https://www.sigmetrics.org/awards.shtml",
    "achievement": [{"year": y, "name": n} for (y, n) in ACHIEVEMENT],
    "risingStar":  [{"year": y, "name": n} for (y, n) in RISING_STAR],
    "testOfTime":  [{"awardYear": ay, "paperYear": py, "title": t, "authors": a} for (ay, py, t, a) in TEST_OF_TIME],
    "bestPaper":   [{"year": y, "title": t, "authors": a, "type": ty} for (y, t, a, ty) in PAPER_AWARDS],
    "doctoral":    [{"year": y, "kind": k, "name": n, "institution": inst, "advisor": adv, "title": ti}
                    for (y, k, n, inst, adv, ti) in DOCTORAL],
}
os.makedirs("data", exist_ok=True)
with open("data/awards.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"Wrote data/awards.json: {len(ACHIEVEMENT)} achievement (to {ACHIEVEMENT[0][0]}), "
      f"{len(RISING_STAR)} rising star (to {RISING_STAR[0][0]}), {len(TEST_OF_TIME)} test-of-time (to {TEST_OF_TIME[0][0]}), "
      f"{len(PAPER_AWARDS)} paper awards (to {PAPER_AWARDS[0][0]}), {len(DOCTORAL)} doctoral")
