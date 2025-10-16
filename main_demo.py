from retriever_agent import RetrieverAgent
from analyst_agent import AnalystAgent

retriever = RetrieverAgent()
retriever.load_data(limit=300)
retriever.build_index()

query = "What was Apple's total revenue in 2019?"
print(f"\n🔍 Câu hỏi: {query}\n")

results = retriever.search(query, k=3)
for r in results:
    print(f"🏅 Rank {r['rank']} (distance={r['distance']:.2f})\n{r['context']}\n")

answer = analyst.analyze(results, query)
print("\n==============================")
print(answer)
print("==============================")