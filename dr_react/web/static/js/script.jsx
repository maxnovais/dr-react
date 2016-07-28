var SnippetForm = React.createClass({
  getInitialState: function() {
    return {title: '', snippet: '', language: '', style: ''};
  },
  handleTitleChange: function(e) {
    this.setState({title: e.target.value});
  },
  handleSnippetChange: function(e) {
    this.setState({snippet: e.target.value});
  },
  handleLanguageChange: function(e) {
    this.setState({language: e.target.value});
  },
  handleStyleChange: function(e) {
    this.setState({language: e.target.value});
  },
  handleSubmit: function(e) {
    e.preventDefault();
    var title = this.state.title.trim();
    var snippet = this.state.snippet.trim();
    var language = this.state.language.trim();
    var style = this.state.style.trim();
    if (!title || !snippet || !language || !style) {
      return;
    }
    this.props.onSnippetSubmit({title: title, snippet: snippet, language: language, style: style});
    this.setState({title: '', snippet: '', language: '', style: ''});
  },
  render: function() {
    return (
      <form className="commentForm" onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Your name"
          value={this.state.author}
          onChange={this.handleAuthorChange}
        />
        <input
          type="text"
          placeholder="Say something..."
          value={this.state.text}
          onChange={this.handleTextChange}
        />
        <input type="submit" value="Post" />
      </form>
    );
  }
});

var SnippetsBox = React.createClass({
  render: function() {
    return (
      <div>
        <SnippetForm onSnippetSubmit={this.handleSubmit} />
        <h1>Minha lista de Snippets</h1>
      </div>)
    }
})

ReactDOM.render(<SnippetsBox />, document.getElementById('container'))
