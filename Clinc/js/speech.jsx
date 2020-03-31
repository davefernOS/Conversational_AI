import React from 'react';
import PropTypes from 'prop-types';

class Speech extends React.Component {
  /* Display number of likes a like/unlike button for one post
   * Reference on forms https://facebook.github.io/react/docs/forms.html
   */

  constructor({ url }) {
    // Initialize mutable state
    super({ url });
    this.state = { comments: [], newcomment: '' };
    this.url = url;
    // This binding is necessary to make `this` work in the callback
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    // Call REST API to get comments
    fetch(this.url, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          comments: data.comments.map(comment => ({
            id: comment.commentid,
            owner: comment.owner,
            owner_show_url: comment.owner_show_url,
            text: comment.text,
          })),
        });
      });
    // .catch((error) => console.log(error));
  }

  handleSubmit(event) {
    // Call REST API to post new comment
    event.preventDefault();
    const { newcomment } = this.state;
    document.getElementById('comment-form').reset();
    fetch(this.url, {
      credentials: 'same-origin',
      headers: { 'Content-Type': 'application/json' },
      method: 'POST',
      body: JSON.stringify({
        text: newcomment,
      }),
    })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState(prevState => ({
          comments: prevState.comments.concat([
            {
              id: data.commentid,
              owner: data.owner,
              owner_show_url: data.owner_show_url,
              text: data.text,
            }]),
          newcomment: '',
        }));
      });
    // .catch((error) => console.log(error));
  }

  handleChange(event) {
    this.setState({ newcomment: event.target.value });
  }

  render() {
    // Render comments
    const { comments } = this.state;
    return (
      <div className="comments">
        {comments.map(comment => (
          <p key={comment.id}>
            <a href={comment.owner_show_url}>
              <b>
                {comment.owner}
              </b>
            </a>
            {comment.text}
          </p>
        ))}
        <form id="comment-form" onSubmit={this.handleSubmit}>
          <input type="text" onChange={this.handleChange} />
        </form>
      </div>
    );
  }
}

Comments.propTypes = {
  url: PropTypes.string.isRequired,
};









export default Speech;