import React from 'react';
import PropTypes from 'prop-types';

class Speech extends React.Component {
  /* Display number of likes a like/unlike button for one post
   * Reference on forms https://facebook.github.io/react/docs/forms.html
   */

  constructor({ url }) {
    // Initialize mutable state
    super({ url });
    this.url = url;
    this.state = { status: "", status_code: "" };
  }

  componentDidMount() {
    // Call REST API
    fetch(this.url, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          status: data.status,
          status_code: data.status_code,
        });
      });
  }

  render() {
    // Render number of likes
    const { status } = this.state;
    return (
      <p>
        "Apple"
      </p>
    );
  }
}

Speech.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Speech;
