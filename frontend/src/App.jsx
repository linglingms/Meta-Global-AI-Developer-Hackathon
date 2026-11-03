function App() {
  return (
    <main className="app-shell">
      <p className="eyebrow">Molecular A(Muse)ing Transcriber</p>
      <h1>Explore scientific data with confidence.</h1>
      <p className="intro">
        A research workspace for connecting biological targets, compounds, and
        experimental evidence.
      </p>
      <section className="target-card" aria-labelledby="target-heading">
        <div>
          <p className="card-label">First target</p>
          <h2 id="target-heading">EGFR</h2>
          <p>Human epidermal growth factor receptor</p>
        </div>
        <span className="status">Ready for research</span>
      </section>
    </main>
  );
}

export default App;
